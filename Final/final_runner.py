"""
TODO
"""
import os

from image_capture import Capture_Image
from mediapipe_hand_test import Get_Landmark_Coordinates
from hand_size_analysis import Get_Hand_Width, Get_Hand_Length

from resize_image import Resize_Design

from svg_gcode import svg_gcode_converter
from img_bitmap import img_bitmap_converter
from bitmap_svg import bitmap_svg_converter

from gcode_processor import separate_lines
from gcode_processor import write_to_serial

# take a picture of the user's hand
Capture_Image()
HAND_IMAGE_FILES = ["Capture_Image.jpg"]

# get width and length landmark coordinates
width_landmarks, length_landmarks = Get_Landmark_Coordinates(HAND_IMAGE_FILES)
print(width_landmarks, length_landmarks)

# get hand width and length
hand_width = Get_Hand_Width(width_landmarks)
hand_length = Get_Hand_Length(length_landmarks)

# resize mehendi design
img_file = "example1.jpg"

Resize_Design(hand_width, hand_length, img_file)
bitmap_file = img_bitmap_converter(img_file)
svg_file = bitmap_svg_converter(bitmap_file)
gcode_file = svg_gcode_converter(svg_file)

os.system("arduino --upload gcode_interpreter/gcode_interpreter.ino --port /dev/ttyACM0")

gcode_file = open("current.gcode")
gcode_array = separate_lines(gcode_file)
write_to_serial(gcode_array)