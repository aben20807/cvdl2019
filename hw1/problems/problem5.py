import torch
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from .model.lenet import LeNet
from .model.dataset import Dataset
from .model.train import Train
from .model.utils import Utils

net = LeNet()
tr = Train(net)

def close_all_plt():
    plt.close('all')

def p5_1(ui):
    Utils.show_10_images_and_images(tr.dataset)

def p5_2(ui):
    print(tr.hyperparam)

def p5_3(ui):
    learn_loss = tr.train(num_epochs=1, sample_rate='iteration')
    plt.ion()
    plt.figure()
    plt.plot(learn_loss)
    plt.ylabel("loss")
    plt.xlabel('epoch')
    plt.show()

def p5_4(ui):
    pretrained_png_path = os.getcwd() + os.sep + "images" + os.sep + "trained.png"
    if os.path.isfile(pretrained_png_path):
        plt.ion()
        plt.figure()
        plt.imshow(mpimg.imread(pretrained_png_path))
        plt.axis('off')
        plt.show()
    else:
        learn_loss = tr.train(num_epochs=50, sample_rate='epoch', save_model=True)
        plt.ion()
        f = plt.figure()
        f.add_subplot(2, 1, 1)
        plt.plot([100-x for x in learn_loss])
        plt.title('Accuracy')
        plt.ylabel("%")
        
        f.add_subplot(2, 1, 2)
        plt.plot(learn_loss)
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.axis('off')
        plt.show()
        plt.savefig(pretrained_png_path)

def p5_5(ui):
    # Get the index from the GUI
    index = int(ui.t5_5_index.text()) if ui.t5_5_index.text().isdigit() else 0
    
    # Get the corresponding test data
    image, label = tr.dataset.get_test(index)
    Utils.image_show(image)
    print("Ground truth: " + str(tr.dataset.get_class_name(label)))

    # Load the pretrained weights
    net.load_state_dict(torch.load(tr.hyperparam.pretrained_model_path))

    # Inference
    output = net(image[None].type('torch.FloatTensor'))
    
    # Get the probability from the prediction output
    probability = torch.nn.functional.softmax(output, dim=1).detach().numpy()[0]

    # Display the probability in bar chart
    plt.ion()
    plt.figure()
    plt.bar(tr.dataset.classes, probability)
    plt.xlabel('classes')
    plt.ylabel('probability')
    plt.show()