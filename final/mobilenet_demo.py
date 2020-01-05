import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils, mobilenet

def process_image(img_path):
    """ process an image to be mobilenet friendly
    """

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    pImg = mobilenet.preprocess_input(img_array)
    return pImg

def _label_preprocess():
    """ process labels
    """

    meta_dir = os.getcwd() + os.sep + "imagenet_meta" + os.sep
    meta_path = meta_dir + "meta.mat"
    synset_path = meta_dir + "synset_words.txt"
    truth_path = meta_dir + "ILSVRC2012_validation_ground_truth.txt"

    meta = scipy.io.loadmat(meta_path)
    original_idx_to_synset = {}
    synset_to_name = {}

    for i in range(1000):
        ilsvrc2012_id = int(meta["synsets"][i,0][0][0][0])
        synset = meta["synsets"][i,0][1][0]
        name = meta["synsets"][i,0][2][0]
        original_idx_to_synset[ilsvrc2012_id] = synset
        synset_to_name[synset] = name

    synset_to_keras_idx = {}
    keras_idx_to_synset = {}
    keras_idx_to_name = {}
    with open(synset_path, "r") as f:
        idx = 0
        for line in f:
            parts = line.split(" ")
            synset_to_keras_idx[parts[0]] = idx
            keras_idx_to_synset[idx] = parts[0]
            keras_idx_to_name[idx] = " ".join(parts[1:]).strip()
            idx += 1

    with open(truth_path, "r") as f:
        vgt = f.read().strip().split('\n')
    vgt = list(map(int, vgt))
    vgt = np.array([synset_to_keras_idx[original_idx_to_synset[idx]] for idx in vgt])
    return vgt, keras_idx_to_name, keras_idx_to_synset

if __name__ == '__main__':
    input_dir = os.getcwd() + os.sep + "images" + os.sep
    output_dir = os.getcwd() + os.sep + "output" + os.sep

    # Define the mobilenet model
    # Source: https://github.com/keras-team/keras-applications/blob/master/keras_applications/mobilenet.py#L87
    net = mobilenet.MobileNet()
    print(net.summary())

    y_test, keras_idx_to_name, keras_idx_to_synset = _label_preprocess()

    for i in range(20):
        # Path to test image
        test_img_path = input_dir + "/ILSVRC2012_val_{:0>8d}.JPEG".format(i+1)

        # Process the test image
        pImg = process_image(test_img_path)

        # Make predictions on test image using mobilenet
        prediction = net.predict(pImg)

        # Obtain the top-5 predictions
        results = imagenet_utils.decode_predictions(prediction, top=5)
        ground_truth = keras_idx_to_synset[y_test[i]]
        # print(results)
        # print(ground_truth)
        pred_synset = [i[0] for i in results[0]]
        pred_labels = [i[1] for i in results[0]]
        pred_probas = [i[2] for i in results[0]]

        # Create colors for the bar graph
        colors = []
        for value in pred_synset:
            if ground_truth == value:
                colors.append('r')
            else:
                colors.append('b')

        # Save the top 5 result for each input
        fig, ax = plt.subplots(figsize=(6,4))
        ax.set_ylim(0, 1)
        ax.bar(pred_labels, pred_probas, color=colors)
        plt.draw()
        for label in ax.get_xticklabels():
            label.set_rotation(30)
            label.set_ha('right')
        ax.set_xlabel('classes')
        ax.set_ylabel('probability')
        ax.figure.savefig(output_dir+"/ILSVRC2012_prob_{:0>8d}.png".format(i+1), bbox_inches='tight')
