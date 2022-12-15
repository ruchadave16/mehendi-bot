"""
TODO
"""
import cv2

def Capture_Image():
    """
    TODO
    """
    # Define which camera to use (0 = webcam)
    videoCaptureObject = cv2.VideoCapture(2)

    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img = cv2.imwrite("Capture_Image.jpg", frame)
        result = False
    videoCaptureObject.release()
