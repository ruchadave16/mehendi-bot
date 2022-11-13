import os

def bitmap_svg_converter(bitmap_file):
    os.system(f"potrace {bitmap_file} -s -o current.svg")
    return "current.svg"