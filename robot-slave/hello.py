#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time

from storage import *
from gate import *
from sensors import *
from brickcomm import *
from mainMovingCompartment import mainCompartment as Steering
from console import *
from arduinocomm import connect

# state constants
ON = True
OFF = False

def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')

    # wait a bit so you have time to look at the display before the program
    # 
    time.sleep(5)

    connect()

if __name__ == '__main__':
    main()
