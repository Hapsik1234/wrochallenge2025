#!/usr/bin/env python3
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent              # type: ignore
from ev3dev2.motor import MediumMotor as SmallMotor                                 # type: ignore


class Storage:
    
    def __init__(self, rotor_port=OUTPUT_A, lift_port=OUTPUT_B):
        
        self.Rotor = SmallMotor(rotor_port) # The spinning sfastika
        self.Lift = LargeMotor(lift_port) # Storage up and down motor

        self.UP = 1
        self.DOWN = -1

        self.GOODDIRECTION = 1
        self.BADDRIERECTION = -1

        # Representation of screws currently loaded in storage bay
        self.GREENSCREW = 1
        self.BLUESCREW = 2
        self.YELLOWSCREW = 3
        self.REDSREW = 4

        self.screws = []



    # Move storage up or down
    # Direction accepts Storage.UP or Storage.DOWN
    def lift(self, direction, speed=70, rotations=3): 

        if not direction:
            speed = -speed
    
        self.Lift.on_for_rotations(SpeedPercent(speed), rotations)
   
    # Rotate storage
    # direction accepts Storage.GOODIRECTION or Storage.BADIRECTION
    def rotate(self, n=1, step=90, speed=SpeedPercent(25), direction=1):
        
        if not direction:
            speed = -speed

        self.Rotor.on_for_degrees(speed, step*n)

    # A complete 
    def load_screws(self):
        #Sensor input required
        
        
        self.lift(self.DOWN)