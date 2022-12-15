"""
TODO
"""

import os

def bitmap_svg_converter(bitmap_file):
    """
    TODO

    Args:
        bitmap_file: A file representing TODO:

    Returns:
    TODO

    """
    os.system(f"potrace {bitmap_file} -s -o current.svg")
    return "current.svg"