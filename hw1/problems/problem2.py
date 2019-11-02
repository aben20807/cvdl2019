import cv2
import os
import numpy as np

def p2_1(ui):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    (chessboard_height, chessboard_width) = (11, 8)
    objp = np.zeros((chessboard_height*chessboard_width,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_height,0:chessboard_width].T.reshape(-1,2)
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    pyramid = np.float32([[0,0,-2], [1,1,0], [1,-1,0], [-1,-1,0], [-1,1,0]]).reshape(-1,3)
    
    img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep
    img_list = []
    for i in range(1, 6):
        img = cv2.imread(filename=img_dir + str(i) + ".bmp")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray_img, (chessboard_height,chessboard_width))
        if ret == True:

            # Used to increase the accuracy of the points
            acc_corners = cv2.cornerSubPix(gray_img, corners, (11,11), (-1,-1), criteria)

            objpoints.append(objp)
            imgpoints.append(acc_corners)
            _, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_img.shape[::-1], None, None)
            _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, acc_corners, cameraMatrix, distCoeffs)
            imgpts, _ = cv2.projectPoints(pyramid, rvecs, tvecs, cameraMatrix, distCoeffs)

            # Draw and save it to the list.
            # Because there was a delay between the processing of the images,
            # storing the drew images and showing them in the next loop
            # were used to handle the delay.
            img = draw_pyramid(img, imgpts)
            img_list.append(img)

    # Show the stored images
    for img in img_list:
        cv2.imshow(str(i)+".bmp", img)
        # Show the image 0.5 seconds and close it
        cv2.waitKey(500)
        cv2.destroyAllWindows()

def draw_pyramid(img, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # Connect top to the corners
    vertex = tuple(imgpts[0].ravel())
    for i in imgpts[1:]:
        img = cv2.line(img, vertex, tuple(i.ravel()), color=(0,0,255), thickness=3)
    # Connect corners
    img = cv2.drawContours(img, [imgpts[1:]], 0, color=(0,0,255), thickness=3)
    return img