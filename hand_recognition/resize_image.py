from PIL import Image

import numpy as np
import time

def resize_design(length_hand, width_hand):
    smaller_hand_edge = min(length_hand, width_hand)

    # get image and determine file type
    filepath = "/home/emascillaro/Documents/Emma/Olin/Sophomore_Year/Fall_Semester/PIE/final_project/mehendi-bot/sprint_2/jpg_svg_gcode/shrek.jpeg"
    filetype_position = filepath.find(".")
    file_type = filepath[filetype_position:]

    # display image
    design_img = Image.open(filepath)
    design_img.show()
    
    # get width and height of the design
    length_design = design_img.height
    width_design = design_img.width

    larger_design_edge = max(length_design, width_design)

    scale_factor = larger_design_edge/smaller_hand_edge

    # resize design to fit into the hand
    # the larger side of the design should be proportionally scaled down to the smaller side of the hand
    resize_design_image = design_img.resize((int(length_design/scale_factor), int(width_design/scale_factor)))

    resize_design_image.save(f"resized{file_type}")
    

resize_design(50, 73)
