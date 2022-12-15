"""
TODO
"""

from image_capture import Capture_Image
from mediapipe_hand_test import Get_Landmark_Coordinates
from hand_size_analysis import Get_Hand_Width, Get_Hand_Length
from resize_image import Resize_Design

# take a picture of the user's hand
#Capture_Image()
IMAGE_FILES = ["Capture_Image.jpg"]

# get width and length landmark coordinates
width_landmarks, length_landmarks = Get_Landmark_Coordinates(IMAGE_FILES)
print(width_landmarks, length_landmarks)

# get hand width and length
hand_width = Get_Hand_Width(width_landmarks)
hand_length = Get_Hand_Length(length_landmarks)
#print (hand_width, hand_length)

# resize mehendi design
Resize_Design(hand_width, hand_length)
