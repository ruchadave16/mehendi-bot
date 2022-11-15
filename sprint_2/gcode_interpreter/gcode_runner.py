from gcode_processor import separate_lines
from gcode_processor import write_to_serial

gcode_file = open("../jpg_svg_gcode/current.gcode")

gcode_array = separate_lines(gcode_file)

write_to_serial(gcode_array)