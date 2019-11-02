import cv2
import os
import numpy as np

from .problem1 import calibrateCameraFromChessboard

(chessboard_height, chessboard_width) = (11, 8)
pyramid = np.float32([[0,0,-2], [1,1,0], [1,-1,0], [-1,-1,0], [-1,1,0]]).reshape(-1,3)
img_dir = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "CameraCalibration" + os.sep

def p2_1(ui):
    drew_img_list = []

    for i in range(1, 6):
        filename = img_dir + str(i) + ".bmp"
        ret = calibrateCameraFromChessboard(filename)
        if ret['patternWasFound'] == True:
            _, rvecs, tvecs, _ = cv2.solvePnPRansac(ret['objp'], ret['corners'], ret['cameraMatrix'], ret['distCoeffs'])
            imgpts, _ = cv2.projectPoints(pyramid, rvecs, tvecs, ret['cameraMatrix'], ret['distCoeffs'])

            # Draw and save it to the list.
            # Because there was a delay between the processing of the images,
            # storing the drew images and showing them in the next loop
            # were used to handle the delay.
            img = draw_pyramid(ret['image'], imgpts)
            drew_img_list.append(img)

    # Show the stored images
    for img in drew_img_list:
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