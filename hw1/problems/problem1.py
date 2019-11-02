import cv2
import os
import numpy as np

img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
(chessboard_height, chessboard_width) = (11, 8)

def close_all_cv():
        cv2.destroyAllWindows()

def calibrateCameraFromChessboard(img_path):
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_height,0:chessboard_width].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    patternWasFound, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
    if patternWasFound == True:
        # Used to increase the accuracy of the points
        corners = cv2.cornerSubPix(
            gray_img, corners, (11,11), (-1,-1), 
            criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001))
        objpoints.append(objp)
        imgpoints.append(corners)
        _, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_img.shape[::-1], None, None)
    return {
        'image': img,
        'patternWasFound': patternWasFound,
        'corners': corners,
        'objp': objp,
        'cameraMatrix': cameraMatrix,
        'distCoeffs': distCoeffs,
        'rvecs': rvecs,
        'tvecs': tvecs,
    }

def p1_1(ui):
    for i in range(1, 16):
        filename = img_dir + str(i) + ".bmp"
        ret = calibrateCameraFromChessboard(filename)
        if ret['patternWasFound'] == True:
            # Draw and display the corners
            img = cv2.drawChessboardCorners(
                ret['image'], (chessboard_height,chessboard_width),
                ret['corners'], ret['patternWasFound'])
            cv2.imshow(str(i)+".bmp", img)

def p1_2(ui):
    for i in range(1, 16):
        filename = img_dir + str(i) + ".bmp"
        ret = calibrateCameraFromChessboard(filename)
        if ret['patternWasFound'] == True:
            np.set_printoptions(formatter={'float': '{:.6f}'.format})
            print(str(i) + ".bmp")
            print(ret['cameraMatrix'])

def p1_3(ui):
    # Get the content of the combo box
    index = int(ui.c1_3.currentText())

    filename = img_dir + str(index) + ".bmp"
    ret = calibrateCameraFromChessboard(filename)
    if ret['patternWasFound'] == True:
        _, rvecs, tvecs, _ = cv2.solvePnPRansac(
            ret['objp'], ret['corners'],
            ret['cameraMatrix'], ret['distCoeffs'])
        # Converts a rotation vector to a rotation matrix
        rmtx, _ = cv2.Rodrigues(rvecs)

        # Combine the rotation matrix and the translation vector
        extrinsic_mtx = np.c_[rmtx, tvecs]
        print(str(index) + ".bmp")
        print(extrinsic_mtx)

def p1_4(ui):
    for i in range(1, 16):
        filename = img_dir + str(i) + ".bmp"
        ret = calibrateCameraFromChessboard(filename)
        if ret['patternWasFound'] == True:
            np.set_printoptions(formatter={'float': '{:.6f}'.format})
            print(str(i) + ".bmp")
            print(ret['distCoeffs'][0])