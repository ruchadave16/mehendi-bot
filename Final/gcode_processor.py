"""
Read G-Code commands from file and print to Serial
"""
from serial import Serial
import time

arduino = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

def separate_lines(gcode_file):
    """
    Separate each G-Code command from a file given into an array of strings

    Args:
        gcode_file: A file containing the G-Code commands to be executed

    Returns:
    An array containing each of the G-Code commands
    """
    return gcode_file.readlines()

def fetch_data():
    """
    Read next line from arduino and decode it

    Returns:
    A string representing the decoded line from Serial
    """
    return arduino.readline().decode()

def write_read(x):
    """
    Write a given command to Serial and obtain the next line printed to Serial. This line is
    written by Arduino, representing the movement that was just executed by the motors

    Args:
        x: A string representing the command to be sent over Serial

    Returns:
    A string representing the command that was just executed by the Arduino
    """
    time.sleep(1.0)
    arduino.write(bytes(x, 'utf-8'))

    print(f"Sent: '{x}'")
    time.sleep(1.0)
    data = fetch_data()

    if data == "\n":
        data = fetch_data()
    return(data)

def write_to_serial(gcode_array):
    """
    Reads each G-Code command and sends it to the Arduino.

    The command is sent via the 'write_read' function and the line printed by the Arduino is
    obtained back. Data continues to be fetched unless the motion has been completed by the
    machine.

    Args:
        gcode_array: An array representing each of the G-Code commands that are to be executed by
            the machine
    """
    gcode_array = ["", "", "", "", "", "", ""] + gcode_array
    arduino.write(bytes("Starting", 'utf-8'))
    time.sleep(1.0)

    for command in gcode_array:
        data = write_read(command)
        print(f"Received: '{data}'")

        while ("G1" or "M") not in data:
            time.sleep(0.5)
            data = fetch_data()
