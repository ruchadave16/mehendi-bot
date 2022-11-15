from gcode_processor import separate_lines
from gcode_processor import write_to_serial

gcode_file = open("/home/emascillaro/Documents/Emma/Olin/Sophomore_Year/Fall_Semester/PIE/final_project/mehendi-bot/sprint_2/jpg_svg_gcode/current.gcode")

gcode_array = separate_lines(gcode_file)
write_to_serial(gcode_array)