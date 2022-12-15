"""
TODO
"""
from PIL import Image

import numpy as np

def Resize_Design(hand_width, hand_length, img_file):
    """
    TODO
    
    Args:
        hand_width: A TODO
        hand_length: A TODO
    """
    smaller_hand_edge = min(hand_width, hand_length)

    # get image and determine file type
    filetype_position = img_file.find(".")
    file_type = img_file[filetype_position:]

    # display image
    design_img = Image.open(img_file)
    
    # get width and height of the design
    design_length = design_img.height
    design_width = design_img.width

    larger_design_edge = max(design_width, design_length)

    scale_factor = larger_design_edge/smaller_hand_edge

    # resize design to fit into the hand
    # the larger side of the design should be proportionally scaled down to the smaller side of the hand
    resize_design_image = design_img.resize((int(design_length/scale_factor), int(design_width/scale_factor)))
    resize_design_image.show()
    resize_design_image.save(f"resized{file_type}")
