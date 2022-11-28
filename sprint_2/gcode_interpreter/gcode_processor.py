from serial import Serial
import time

arduino = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

null_list = ["", "\n", "done"]

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    print(f"Sent: {x}")
    time.sleep(0.05)
    data = ""
    while data in null_list:
        data = arduino.readline().decode()
    return data
    # print(data)
    # while data != "done":
    #     time.sleep(0.5)
    # return data

def separate_lines(gcode_file):
    return gcode_file.readlines()

def write_to_serial(gcode_array):
    for command in gcode_array:
        answer = write_read(command)
        print(f"Received: {answer}")
