"""
TODO
"""

import cv2
import numpy as np

def changeRes(width, height):
    """
    TODO Rescaling Function

    Args:
        width: TODO
        height: TODO
    """
    # Only works for live videos
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)

# Empty placeholder function
def empty(a):
    pass

# Get contour function
def getContours(img, img_contour):
    """
    TODO

    Args:
        img: TODO
        img_contour: TODO
    """
    contours, hierachies = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_contour, contours, -1, (255,0,255), 3)
    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     if area > 1000:
    #         cv2.drawContours(imgContour, cnt, -1, (255,0,255), 3)

# def getAreaBox()
# Live video reading
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(2)

# Generalize Resolution
changeRes(frameWidth, frameHeight)

# # Sliders initialization for canny threshold values
# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 150, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)

# Video Display
while True:
    success, img = cap.read()
    imgContour = img.copy()
    blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    # Threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    # Threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    # canny_test = cv2.Canny(gray, Threshold1, Threshold2)
    # cv2.imshow("Canny Testing", cv2.flip(canny_test, 1))

    canny = cv2.Canny(gray, 96, 29)
    dilated = cv2.dilate(canny, (5, 5), iterations=3)

    getContours(dilated, imgContour)

    cv2.imshow("Processed Video", cv2.flip(imgContour, 1))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
