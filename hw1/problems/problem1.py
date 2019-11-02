import cv2
import os
import numpy as np

def close_all_cv():
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
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    (chessboard_height, chessboard_width) = (11, 8)
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_height,0:chessboard_width].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
    for i in range(1, 16):
        img = cv2.imread(filename=img_dir + str(i) + ".bmp")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
        if ret == True:
            
            # Used to increase the accuracy of the points
            acc_corners = cv2.cornerSubPix(gray_img, corners, (11,11), (-1,-1), criteria)
            
            objpoints.append(objp)
            imgpoints.append(acc_corners)
            _, cameraMatrix, _, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_img.shape[::-1], None, None)
            np.set_printoptions(formatter={'float': '{:.6f}'.format})
            print(str(i) + ".bmp")
            print(cameraMatrix)

def p1_3(ui):
    # Get the content of the combo box
    index = int(ui.c1_3.currentText())

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    (chessboard_height, chessboard_width) = (11, 8)
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_height,0:chessboard_width].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
    img = cv2.imread(filename=img_dir + str(index) + ".bmp")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
    if ret == True:

        # Used to increase the accuracy of the points
        acc_corners = cv2.cornerSubPix(gray_img, corners, (11,11), (-1,-1), criteria)

        objpoints.append(objp)
        imgpoints.append(acc_corners)
        _, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_img.shape[::-1], None, None)
        _, rvecs, tvecs, _ = cv2.solvePnPRansac(objp, acc_corners, cameraMatrix, distCoeffs)

        # Converts a rotation vector to a rotation matrix
        rmtx, _ = cv2.Rodrigues(rvecs)

        # Combine the rotation matrix and the translation vector
        extrinsic_mtx = np.c_[rmtx, tvecs]
        print(extrinsic_mtx)

def p1_4(ui):
    print("ouo")
    ui.t3_1_angle.setText("OuO")