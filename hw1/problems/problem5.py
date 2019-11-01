import torch.optim as optim
import torch
import torch.nn as nn
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from .model import lenet, dataset, hyperparam, train

hp = hyperparam.Hyperparam(
    batch_size=64,
    learning_rate=0.001,
    optimizer=optim.SGD,
    loss_fn=nn.CrossEntropyLoss,
    pretrained_model_path=os.getcwd() + os.sep + "problems" + os.sep + "model" + os.sep + "lenet_cifar10.pth")
ds = dataset.Dataset(hp.batch_size);
net = lenet.LeNet()

def close_all_plt():
    plt.close('all')

def p5_1(ui):
    ds.show_10_images_and_images()

def p5_2(ui):
    print(hp)

def p5_3(ui):
    tr = train.Train(hp, net, ds.trainloader)
    learn_loss = tr.train(num_epochs=1, sample_rate='iteration')
    plt.ion()
    plt.figure()
    plt.plot(learn_loss)
    plt.ylabel("loss")
    plt.xlabel('epoch')
    plt.show()

def p5_4(ui):
    pretrained = os.getcwd() + os.sep + "images" + os.sep + "trained.png"
    if os.path.isfile(pretrained):
        plt.ion()
        plt.figure()
        img = mpimg.imread(pretrained)
        imgplot = plt.imshow(img)
        plt.show()
    else:
        tr = train.Train(hp, net, ds.trainloader)
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
        plt.show()
        plt.savefig(pretrained)

def p5_5(ui):
    index = int(ui.t5_5_index.text()) if ui.t5_5_index.text().isdigit() else 0
    image, label = ds.get_test(index)
    ds.image_show(image)
    print("Ground truth: " + str(ds.classes[label]))

    # Load the pretrained weights
    net.load_state_dict(torch.load(hp.pretrained_model_path))

    # Inference
    output = net(image[None].type('torch.FloatTensor'))
    
    # Get the probability from the prediction output
    probability = torch.nn.functional.softmax(output, dim=1).detach().numpy()[0]

    # Display the bar chart
    plt.ion()
    plt.figure()
    plt.bar(ds.classes, probability)
    plt.xlabel('classes')
    plt.ylabel('probability')
    plt.show()