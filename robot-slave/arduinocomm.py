import serial # type: ignore
import time, threading
from random import random
from console import debug_print
distance_right = -1
distance_left = -1

arduino_ready = False

ICODE = "b4115erwin"
sensorreadingsprefix = "sens."

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def format_response(a_response):
    entire_prefix = ICODE + "I" + sensorreadingsprefix
    if a_response.startswith(entire_prefix):
        a_response = a_response.replace(entire_prefix, "")
        return a_response.split(", ")
    else:
        return [-1, -1]

def read(arduinoserial):

    while True:
        res = arduinoserial.readline()
        debug_print(b'<Arduino> ' + res.decode().strip())

        res = res.decode().strip()

        if (res.startswith(ICODE)):
            message = remove_prefix(res, ICODE)
            code = message.split(".")[0]
            message = message.split(".")[1]

            if code == "Isens":
                distance_right, distance_left = format_response(message.decode().strip())
            else:
                if code[0]=="I":
                    debug_print(b'Debug information from arduino: ' + code[1:])
                elif code[0]=="S":
                    debug_print(b'Debug success from arduino: ' + code[1:])
                elif code[0]=="E":
                    debug_print(b'Debug error from arduino: ' + code[1:])
                else:
                    debug_print(code)

async def connect():
    # Open the serial port
    ser = serial.Serial('/dev/ttyACM0', 9600)
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



    # distance_right, distance_left = format_response(response.decode().strip())

    ser.close()