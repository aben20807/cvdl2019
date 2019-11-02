import os
import torch
import torch.nn as nn
import torch.optim as optim

from .hyperparam import Hyperparam
from .dataset import Dataset

class Train(object):
    def __init__(self, net):
        self.net = net
        self.hyperparam = Hyperparam(
            batch_size=64,
            learning_rate=0.001,
            optimizer=optim.SGD,
            loss_fn=nn.CrossEntropyLoss,
            pretrained_model_path=os.getcwd() + \
                os.sep + "problems" + \
                os.sep + "model" + \
                os.sep + "lenet_cifar10.pth")
        self.dataset = Dataset(self.hyperparam.batch_size);

    def train(self, num_epochs, sample_rate, save_model=False):
        epochs_size = len(self.dataset.trainloader)
        learn_loss = []
        print('Start Training')
        opt = self.hyperparam.optimizer(self.net.parameters(), lr=self.hyperparam.learning_rate)
        criterion = self.hyperparam.loss_fn()
        for epoch in range(num_epochs):
            running_loss = 0.0
            
            for i, data in enumerate(self.dataset.trainloader, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data

                # zero the parameter gradients
                opt.zero_grad()

                # forward + backward + optimize
                outputs = self.net(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                opt.step()

                # print statistics
                if sample_rate == 'iteration':
                    learn_loss.append(loss.item())
                running_loss += loss.item()

            if sample_rate == 'epoch':
                learn_loss.append(running_loss/epochs_size)
                print('[%d] loss: %.3f' %
                  (epoch + 1, running_loss/epochs_size))
        if save_model:
            torch.save(self.net.state_dict(), self.hyperparam.pretrained_model_path)

        print('Finished Training')
        return learn_loss