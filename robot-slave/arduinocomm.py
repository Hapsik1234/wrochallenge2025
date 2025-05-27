import serial # type: ignore  
import time, threading
from random import random
from console import debug_print
from ev3dev2.button import Button


ser = serial.Serial('/dev/ttyACM0', 9600)

arduino_ready = False

ICODE = "b4115erwin"
sensorreadingsprefix = "sens."
class SensorReadings:
    def __init__(self, distance_left, distance_right, arduino_ready=False):
        self.distance_left = distance_left
        self.distance_right = distance_right
        self.arduino_ready = False
        self.senosors_ready = False
    
sensor_readings = SensorReadings(-1, -1)

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def format_response(a_response):
    return map(int, a_response.split(", "))


def read():

    while True:
        res = ser.readline()
        res = res.decode().strip()

        res = str(res)
        # debug_print('<Arduino> ' + res)

        

        if (res.startswith(ICODE)):
            message = remove_prefix(res, ICODE)
            code = message.split(".")[0]
            message = message.split(".")[1]

            if code == "Isens":
                sensor_readings.distance_right, sensor_readings.distance_left =  format_response(message)
                debug_print(str(sensor_readings.distance_left) + " mm left, " + str(sensor_readings.distance_right) + " mm right")
            elif code == "Ss1wait":
                sensor_readings.arduino_ready = True
                debug_print("Arduino sensor 1 is ready!")
            else:
                if code[0]=="I":
                    debug_print('Debug information from arduino: ' + code[1:])
                elif code[0]=="S":
                    debug_print('Debug success from arduino: ' + code[1:])
                elif code[0]=="E":
                    debug_print('Debug error from arduino: ' + code[1:])
                else:
                    debug_print(code)

def connect():
    # Open the serial port
    
    time.sleep(2)  # Wait for the Arduino to reset

    # Test arduino
    ser.write(b'Hello Arduino\n')
    response = ser.readline()
    print("Received:", response.decode().strip())

    # Run thread for asyncronous reading

    t = threading.Thread(target=read)
    t.start()

    # Start

    ser.write(b'c\n')

    # Wait for Arduino initalization of sensor 1
    while sensor_readings.arduino_ready == False:
        time.sleep(0.005)
    print("Arduino is ready!")

    btn = Button()

    while True:
        if btn.enter:
            print("Center button pressed!")
            break
        time.sleep(0.1)

    ser.write(b'c\n')

    time.sleep(1)

    ser.write(b'startsensing\n')
    sensor_readings.senosors_ready = True

    # distance_right, distance_left = format_response(response.decode().strip())

    # ser.close()