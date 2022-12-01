from serial import Serial
import time

arduino = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

def fetch_data():
    data = arduino.readline().decode()
    return data

null_list = []

def write_read(x):
    check_ready = ''
    while check_ready != "Next":
        print(f'"{check_ready}"')
        check_ready = fetch_data()

    arduino.write(bytes(x, 'utf-8'))
    print(f"Sent: {x}")
    time.sleep(0.5)
    data = fetch_data()

    while (len(data) == 0):
        print("In Null List")
        data = fetch_data()
    print(f"Data is: '{data}'")
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
        # print(f"Received: {answer}")
