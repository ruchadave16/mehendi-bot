from PIL import Image

import numpy as np
import time

def resize_design(length_hand, width_hand):
    larger_design_edge = max(length_hand, width_hand)

    # get image
    filepath = "/home/emascillaro/Documents/Emma/Olin/Sophomore_Year/Fall_Semester/PIE/final_project/mehendi-bot/sprint_2/jpg_svg_gcode/shrek.jpeg"
    design_img = Image.open(filepath)
    
    # display image
    design_img.show()
    
    # get width and height
    length_design = design_img.height
    width_design = design_img.width

    print(length_design)
    print(width_design)

    smaller_hand_edge = min(length_design, width_design)

resize_design(5, 9)
