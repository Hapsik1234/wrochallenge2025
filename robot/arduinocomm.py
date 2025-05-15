import serial
import time


def connect():
    # Open the serial port
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)  # Wait for the Arduino to reset

    # Send data
    ser.write(b'Hello Arduino!\n')

    # Read response
    response = ser.readline()
    print("Received:", response.decode().strip())

    ser.close()