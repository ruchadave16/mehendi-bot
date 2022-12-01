from serial import Serial
import time

arduino = Serial(port='/dev/ttyACM1', baudrate=115200, timeout=.1)

def fetch_data():
    return arduino.readline().decode()

null_list = []

def write_read(x):
    check_ready = ''
    while "Next" not in check_ready:
        check_ready = fetch_data()
        print(check_ready)
    print("DONE")

    time.sleep(1.0)
    arduino.write(bytes(x, 'utf-8'))
    print(f"Sent: {x}")
    time.sleep(1.0)
    data = fetch_data()
    if data == "\n":
        data = fetch_data()
    return(data)

    

    
    # time.sleep(0.5)
    # data = fetch_data()

    # # while (len(data) == 0):
    # # data = fetch_data()
    # # print(data)
    # print(f"Data is: '{data}'")
    # return data
    # #     # print(data)
    # #     # while data != "done":
    # #     #     time.sleep(0.5)
    # #     # return data

def separate_lines(gcode_file):
    return gcode_file.readlines()

def write_to_serial(gcode_array):
    gcode_array = ["", "", "", "", "", "", ""] + gcode_array
    for command in gcode_array:
        answer = write_read(command)
        print(f"Received: '{answer}'")
