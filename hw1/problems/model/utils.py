import torchvision
import matplotlib.pyplot as plt
import numpy as np

class Utils(object):

    @staticmethod
    def image_show(img):
        img = img / 2 + 0.5     # unnormalize
        plt.ion()
        plt.figure()
        plt.imshow(np.transpose(img.numpy(), (1, 2, 0)))
        plt.axis('off')
        plt.show()

    @staticmethod
    def show_10_images_and_images(dataset):
        # Get some random training images
        images, labels = iter(dataset.trainloader).next()

        # Print labels
        print("Label: " + '\t'.join('%s' % dataset.classes[labels[i]] for i in range(10)))
        # Show images
        Utils.image_show(torchvision.utils.make_grid(images[:10], nrow=10))