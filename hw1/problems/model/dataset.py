import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

from . import hyperparam

class Dataset(object):
    def __init__(self, batch_size):
        self.transform = transforms.Compose(
            [transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        self.trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                                download=True, transform=self.transform)
        self.trainloader = torch.utils.data.DataLoader(self.trainset, batch_size=batch_size,
                                                shuffle=True, num_workers=2)
        self.testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                            download=True, transform=self.transform)
        self.testloader = torch.utils.data.DataLoader(self.testset, batch_size=batch_size,
                                                shuffle=False, num_workers=2)
        self.classes = ('plane', 'car', 'bird', 'cat',
                        'deer', 'dog', 'frog', 'horse',
                        'ship', 'truck')

    def image_show(self, img):
        img = img / 2 + 0.5     # unnormalize
        plt.ion()
        plt.figure()
        plt.imshow(np.transpose(img.numpy(), (1, 2, 0)))
        plt.axis('off')
        plt.show()

    def show_10_images_and_images(self):
        # get some random training images
        images, labels = iter(self.trainloader).next()

        # print labels
        print("Label: " + '\t'.join('%s' % self.classes[labels[j]] for j in range(10)))
        # show images
        self.image_show(torchvision.utils.make_grid(images[:10], nrow=10))

    def get_test(self, idx):
        return self.testset[idx]