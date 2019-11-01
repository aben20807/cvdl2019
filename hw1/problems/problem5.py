from .model import lenet, dataset, hyperparam

hp = hyperparam.Hyperparam(batch_size=32,learning_rate=0.001,optimizer='SGD')
ds = dataset.Dataset(hp);

def p5_1(ui):
    ds.show_10_images_and_images()

def p5_2(ui):
    print(hp)

def p5_3(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p5_4(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p5_5(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")