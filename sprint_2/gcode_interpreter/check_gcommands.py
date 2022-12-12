"""
Obtain list of all commands in G-Code file
"""
from gcode_processor import separate_lines

g_command_list = []

gcode_file = open("../jpg_svg_gcode/current.gcode")
gcode_array = separate_lines(gcode_file)

for command in gcode_array:
    if ' ' in command:
        beg = command[:command.index(' ')]
    else:
        beg = command
    
    if beg not in g_command_list:
        g_command_list.append(beg)

print(g_command_list)
