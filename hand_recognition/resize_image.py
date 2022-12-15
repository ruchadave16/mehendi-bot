from PIL import Image

import numpy as np

def Resize_Design(hand_width, hand_length):
    smaller_hand_edge = min(hand_width, hand_length)

    # get image and determine file type
    filepath = "/home/emascillaro/Documents/Emma/Olin/Sophomore_Year/Fall_Semester/PIE/final_project/mehendi-bot/sprint_2/jpg_svg_gcode/mehendi_design_1.jpg"
    filetype_position = filepath.find(".")
    file_type = filepath[filetype_position:]

    # display image
    design_img = Image.open(filepath)
    
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
