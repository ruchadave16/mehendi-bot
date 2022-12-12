"""
TODO
"""

import cv2
import numpy as np

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


# Generalize Resolution
changeRes(frameWidth, frameHeight)

# Video Display
while True:
    success, img = cap.read()
    imgContour = img.copy()
    blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 96, 29)
    dilated = cv2.dilate(canny, (5, 5), iterations=3)

    getContours(dilated, imgContour)

    cv2.imshow("Processed Video", cv2.flip(imgContour, 1))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
