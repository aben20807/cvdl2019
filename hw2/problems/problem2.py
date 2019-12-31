import numpy as np
import cv2
import matplotlib.pyplot as plt

def p2_1(ui):
    """ Normalized Cross Correlation
    """

    img_rgb = cv2.imread(ui.img_dir+'ncc_img.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(ui.img_dir+'ncc_template.jpg', 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCORR_NORMED)
    threshold = 0.999
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + template.shape[0], pt[1] + template.shape[1]), (0,0,0), 2)

    f = plt.figure(figsize=[20,10])
    f.add_subplot(1, 2, 2)
    plt.axis('off')
    plt.imshow(res, 'gray')

    f.add_subplot(1, 2, 1)
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

    plt.show()