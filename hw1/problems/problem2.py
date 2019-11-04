import cv2
import os
import numpy as np

from . import problem1

def draw_pyramid(img, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    vertex = tuple(imgpts[0].ravel())
    # Connect top vertex to the bottom contours
    for i in imgpts[1:]:
        img = cv2.line(img, vertex, tuple(i.ravel()), color=(0,0,255), thickness=3)
    # Connect the bottom contours
    img = cv2.drawContours(img, [imgpts[1:]], 0, color=(0,0,255), thickness=3)
    return img

def p2_1(ui):
    # Load some preprocessed data from problem1
    images = problem1.images
    find_ret = problem1.find_ret
    cali_ret = problem1.cali_ret

    for i in range(5):
        if find_ret['patternWasFounds'][i] == True:
            _, rvec, tvec, _ = cv2.solvePnPRansac(
                find_ret['objpoints'][i], find_ret['imgpoints'][i],
                cali_ret['cameraMatrix'], cali_ret['distCoeffs'])
            
            # Project the pyramid
            pyramid = np.float32([[0,0,-2], [1,1,0], [1,-1,0], [-1,-1,0], [-1,1,0]]).reshape(-1,3)
            imgpts, _ = cv2.projectPoints(
                pyramid, rvec, tvec, 
                cali_ret['cameraMatrix'], cali_ret['distCoeffs'])

            # Draw pyramid
            img = draw_pyramid(images[i], imgpts)
            
            # Show the image 0.5 seconds and close it
            img = cv2.resize(img, (900,900))
            cv2.imshow(str(i+1)+".bmp", img)
            cv2.waitKey(500)
            cv2.destroyAllWindows()