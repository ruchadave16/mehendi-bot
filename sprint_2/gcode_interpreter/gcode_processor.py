from serial import Serial
import time

def separate_lines(gcode_file):
    return gcode_file.readlines()

def write_to_serial(gcode_array):

    ser = Serial('/dev/ttyACM0', 115200, timeout=0.050)

    for command in gcode_array:
        ser.write(str.encode(command))
        print(f"{command} sent")
