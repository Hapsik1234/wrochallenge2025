import os
import sys
import time

# from brickcomm import *  # deprecated
from arduinocomm import *

from storage import *
from gate import *
from sensors import *
from mainMovingCompartment import main_compartment as Steering
from console import *


# state constants
ON = True
OFF = False



def main():
    # --------------
    # INIT
    # --------------

    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    print('Hello World!')
    debug_print('Hello VS Code!')

    _storage = Storage()
    _moving = main_compartment()

    _sensors = Sensors(brick_sensors_motor)
    _gate = Gate(brick_gate_motor)

    # --------------
    # ACTUAL CODE
    # --------------

    _storage.lift(_storage.UP)
    
    

if __name__ == '__main__':
    main()