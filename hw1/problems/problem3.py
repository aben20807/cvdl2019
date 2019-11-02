import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def p3_1(ui):
    # Get the index from the GUI
    angle = float(ui.t3_1_angle.text()) if isfloat(ui.t3_1_angle.text()) else 0.0
    scale = float(ui.t3_1_scale.text()) if isfloat(ui.t3_1_scale.text()) else 1.0
    tx = float(ui.t3_1_tx.text()) if isfloat(ui.t3_1_tx.text()) else 0.0
    ty = float(ui.t3_1_ty.text()) if isfloat(ui.t3_1_ty.text()) else 0.0

    # Read the image
    filename = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "OriginalTransform.png"
    img = cv2.imread(filename)
    height, width = img.shape[:2]
    center = (130, 125)
    
    # Rotation and Scaling
    M = cv2.getRotationMatrix2D(center, angle, scale)
    new_img = cv2.warpAffine(img, M, (width,height))

    # Translation
    M = np.float32([[1,0,tx],[0,1,ty]])
    new_img = cv2.warpAffine(new_img, M, (width,height))

    plt.ion()
    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.figure()
    plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()