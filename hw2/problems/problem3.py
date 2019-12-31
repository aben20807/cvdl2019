import cv2
import matplotlib.pyplot as plt

img = []
gray = []
keypoints = []
descriptors = []

def init(ui):
    """
    """
    for i in range(2):
        img.append(cv2.imread(ui.img_dir+'Aerial'+str(i+1)+'.jpg'))
        gray.append(cv2.cvtColor(img[i], cv2.COLOR_BGR2GRAY))
        sift = cv2.xfeatures2d.SIFT_create()

        # Detect the keypoints then sorted by the size before being computed the descriptors
        tmp_kp = sift.detect(gray[i])
        tmp_kp_sort = sorted(tmp_kp, key = lambda x: x.size, reverse = True)[0:7]
        tmp_kp_sort, tmp_des_sort = sift.compute(gray[i], tmp_kp_sort)

        keypoints.append(tmp_kp_sort)
        descriptors.append(tmp_des_sort)

def p3_1(ui):
    """ Find the keypoints

    Find 6 feature points on each Aerial1.jpg and Aerial2.jpg then save results
    """

    plt.show()
    for i in range(2):
        result_img = cv2.drawKeypoints(gray[i], keypoints[i], img[i], color=(0,0,255))
        cv2.imwrite(ui.img_dir+'FeatureAerial'+str(i+1)+'.jpg', result_img)
        cv2.imshow('FeatureAerial'+str(i+1)+'.jpg', result_img)

def p3_2(ui):
    """ Match the keypoints

    draw the matched feature points between two images from 6 keypoints pairs obtained in Q: 3.1
    """
    
    # Find the matches
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors[0], descriptors[1], k=2)

    # Preserve the good matches
    good_matches = []
    for m,n in matches:
        if m.distance < 0.70*n.distance:
            good_matches.append([m])

    # Draw the matches
    img3 = cv2.drawMatchesKnn(gray[0], keypoints[0], gray[1], keypoints[1], good_matches, None, matchColor=(0,255,0), singlePointColor=(0,0,255))
    cv2.imshow("img3", img3)