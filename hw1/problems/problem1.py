import cv2
import os
import numpy as np

def close_all():
        cv2.destroyAllWindows()

def p1_1(ui):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    (chessboard_height, chessboard_width) = (11, 8)
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_width,0:chessboard_height].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    for i in range(1, 16):
        filename = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep + str(i) + ".bmp"
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (chessboard_height,chessboard_width), None)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (chessboard_height,chessboard_width), corners2,ret)
            img = cv2.resize(img, (960,540))
            cv2.imshow("img" + str(i), img)

def p1_2(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p1_3(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")

def p1_4(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")