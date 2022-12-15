"""
"""
from serial import Serial
import time

arduino = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

def fetch_data():
    """
    """
    return arduino.readline().decode()

def write_read(x):
    """
    """

    time.sleep(1.0)
    arduino.write(bytes(x, 'utf-8'))
    print(f"Sent: {x}")
    time.sleep(1.0)
    data = fetch_data()

    if data == "\n":
        data = fetch_data()
    return(data)

def separate_lines(gcode_file):
    """
    """
    return gcode_file.readlines()

def write_to_serial(gcode_array):
    """
    """
    gcode_array = ["", "", "", "", "", "", ""] + gcode_array
    arduino.write(bytes("Starting", 'utf-8'))
    time.sleep(1.0)

    for command in gcode_array:
        if command[0:2] == "G1":
            data = write_read(command)
            print(f"Received: '{data}'")

            while "G1" not in data:
                time.sleep(0.5)
                data = fetch_data()
