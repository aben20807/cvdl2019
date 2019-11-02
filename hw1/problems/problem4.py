import os
import cv2

def p4_1(ui):
    # Read the image
    filename = os.getcwd() + os.sep + "images" + os.sep + "images" + os.sep + "Contour.png"
    img = cv2.imread(filename)

    # Image preprocessing
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray_img, 30, 200)

    # Find the contours
    _, contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Draw the contours and show the result
    cv2.drawContours(img, contours, -1, (0, 0, 255), 3) 
    cv2.imshow('Result Image', img)