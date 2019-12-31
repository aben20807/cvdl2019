import cv2
import matplotlib.pyplot as plt

def p1_1(ui):
    """ Disparity Map

    Given: a pair of images, imL.png and imR.png (have been rectified)
    Q: Find the disparity map/image based on Left and Right stereo images.
    """

    imL = cv2.imread(ui.img_dir+'imL.png', 0)
    imR = cv2.imread(ui.img_dir+'imR.png', 0)

    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
    disparity = stereo.compute(imL, imR)
    plt.imshow(disparity, 'gray')
    plt.axis('off')
    plt.show()