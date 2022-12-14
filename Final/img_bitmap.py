"""
TODO
"""

from PIL import Image
import numpy as np

def img_bitmap_converter(img_file):
    """
    TODO

    Args:
        img_file: A file containing the image to be converted into a bitmap
    
    Returns: 
    TODO
    """

    img = Image.open(img_file)
    ary = np.array(img)

    # Split the three channels
    r,g,b = np.split(ary,3,axis=2)
    r=r.reshape(-1)
    g=r.reshape(-1)
    b=r.reshape(-1)

    # Standard RGB to grayscale 
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
    zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    im.save("current.bmp")
    return "current.bmp"
    