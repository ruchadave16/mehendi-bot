from jpg_svg import jpg_svg_converter
from svg_gcode import svg_gcode_converter

jpg_file = ["Cat03.jpg"]
svg_file = jpg_svg_converter(jpg_file)
gcode_file = svg_gcode_converter(svg_file)