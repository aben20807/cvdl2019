import cv2
import os
import numpy as np

def close_all():
        cv2.destroyAllWindows()

def p1_1(ui):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    (chessboard_height, chessboard_width) = (11, 8)
    img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
    for i in range(1, 16):
        img = cv2.imread(filename=img_dir + str(i) + ".bmp")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
        if ret == True:
            # Used to increase the accuracy of the points
            corners = cv2.cornerSubPix(gray_img, corners, (11,11), (-1,-1), criteria)
            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (chessboard_height,chessboard_width), corners, ret)
            cv2.imshow(str(i)+".bmp", img)

def p1_2(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p1_3(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p1_4(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")