import os
import cv2
import numpy as np

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

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotation + Scale + Translation Image", new_img)

def click_point(event, x, y, flags, pressed_points):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("%d (%d, %d)" % (len(pressed_points)+1, x, y))
        pressed_points.append([x,y])

def p3_2(ui):
    # Read the image
    image_name = "OriginalPerspective.png"
    filename = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + image_name
    img = cv2.imread(filename)
    cv2.imshow(image_name, img)

    # Collect four clicked points
    pressed_points = []
    cv2.setMouseCallback(image_name, click_point, pressed_points)
    while True: # Wait until four points were clicked
        cv2.waitKey(1)
        if len(pressed_points) == 4:
            break
    cv2.destroyAllWindows()

    # Perspective Transform
    src = np.array(pressed_points, np.float32)
    dst = np.array([[20, 20], [450, 20], [450, 450], [20, 450]], np.float32)
    M = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, M, (1000, 1000))
    # Show result image
    cv2.imshow("Perspective Result Image", result)