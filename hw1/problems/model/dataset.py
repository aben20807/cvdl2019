import torch
import torchvision
import torchvision.transforms as transforms

class Dataset(object):
    def __init__(self, batch_size):
        self.transform = transforms.Compose(
            [transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        self.trainset = torchvision.datasets.CIFAR10(
            root='./data',
            train=True,
            download=True,
            transform=self.transform)
        self.trainloader = torch.utils.data.DataLoader(
            self.trainset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=2)
        self.testset = torchvision.datasets.CIFAR10(
            root='./data',
            train=False,
            download=True,
            transform=self.transform)
        # self.testloader = torch.utils.data.DataLoader(
        #     self.testset,
        #     batch_size=batch_size,
        #     shuffle=False,
        #     num_workers=2)
        self.classes = (
            'plane', 'car', 'bird', 'cat', 'deer',
            'dog', 'frog', 'horse', 'ship', 'truck')

    def get_test(self, idx):
        return self.testset[idx]

    def get_class_name(self, label):
        return self.classes[label]