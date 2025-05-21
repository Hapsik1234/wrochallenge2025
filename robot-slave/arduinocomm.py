import serial
import time
from random import random

distance1 = -1
distance2 = -1

def format_response(a_response):
    return a_response.split(",")


def connect():
    # Open the serial port
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)  # Wait for the Arduino to reset

    # Send data
    ser.write(b'Hello Arduino!\n')

    # Read response
    response = ser.readline()
    print("Received:", response.decode().strip())

    distance1, distance2 = format_response(response.decode().strip())

    
    

    ser.close()