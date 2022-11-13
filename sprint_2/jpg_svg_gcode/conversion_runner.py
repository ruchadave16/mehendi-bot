from svg_gcode import svg_gcode_converter
from img_bitmap import img_bitmap_converter
from bitmap_svg import bitmap_svg_converter

img_file = "shrek.jpeg"
bitmap_file = img_bitmap_converter(img_file)
svg_file = bitmap_svg_converter(bitmap_file)
gcode_file = svg_gcode_converter(svg_file)