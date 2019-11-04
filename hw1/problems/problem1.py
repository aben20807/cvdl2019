import cv2
import os
import numpy as np

np.set_printoptions(formatter={'float': '{:.6f}'.format})
# Shape of the chessboard
(chessboard_height, chessboard_width) = (11, 8)

def close_all_cv():
    cv2.destroyAllWindows()

def load_images(img_dir):
    images = []
    for i in range(1, 16):
        filename = img_dir + str(i) + ".bmp"
        images.append(cv2.imread(filename))
    return images

def find_points(images):
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_height,0:chessboard_width].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    patternWasFounds = []
    for img in images:
        # Grayscale and find the points in the chessboard
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        patternWasFound, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
        if patternWasFound == True:
            # Used to increase the accuracy of the points
            corners = cv2.cornerSubPix(
                gray_img, corners, (11,11), (-1,-1), 
                criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001))
            # Store in the list for return later
            objpoints.append(objp)
            imgpoints.append(corners)
            patternWasFounds.append(patternWasFound)
    return {
        'objpoints': objpoints,
        'imgpoints': imgpoints, 
        'patternWasFounds': patternWasFounds,
    }

def calibrate(objpoints, imgpoints):
    _, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, images[0][0].shape[::-1], None, None)
    return {
        'cameraMatrix': cameraMatrix,
        'distCoeffs': distCoeffs,
        'rvecs': rvecs,
        'tvecs': tvecs,
    }

# Load the images and calibrate the camera at the initial phase
img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
images = load_images(img_dir)
find_ret = find_points(images)
cali_ret = calibrate(find_ret['objpoints'], find_ret['imgpoints'])

def p1_1(ui):
    """ Corner Detection
    """
    for idx, img in enumerate(images):
        # Draw and display the corners
        drew_img = cv2.drawChessboardCorners(
            img, (chessboard_height,chessboard_width),
            find_ret['imgpoints'][idx], find_ret['patternWasFounds'][idx])
        cv2.imshow(str(idx+1)+".bmp", drew_img)

def p1_2(ui):
    """ Find the Intrinsic Matrix
    """
    print(cali_ret['cameraMatrix'])

def p1_3(ui):
    """ Find the Extrinsic Matrix
    """
    # Get the content of the combo box
    index = int(ui.c1_3.currentText())
    
    _, rvec, tvec, _ = cv2.solvePnPRansac(
        find_ret['objpoints'][index], find_ret['imgpoints'][index],
        cali_ret['cameraMatrix'], cali_ret['distCoeffs'])
    # Converts a rotation vector to a rotation matrix
    rmtx, _ = cv2.Rodrigues(rvec)

    # Combine the rotation matrix and the translation vector
    extrinsic_mtx = np.c_[rmtx, tvec]
    print(str(index) + ".bmp")
    print(extrinsic_mtx)

def p1_4(ui):
    """ Find the Distortion Matrix
    """
    print(cali_ret['distCoeffs'])