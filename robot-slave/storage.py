#!/usr/bin/env python3
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent              # type: ignore
from ev3dev2.motor import MediumMotor as SmallMotor                                 # type: ignore

class Storage:
    
    def __init__(self, rotor_port=OUTPUT_B, lift_port=OUTPUT_A):
        
        self.Rotor = SmallMotor(rotor_port) # The spinning sfastika
        self.Lift = LargeMotor(lift_port) # Storage up and down motor


        self.UP = 1
        self.DOWN = -1

        self.GOODDIRECTION = 1
        self.BADDRIERECTION = -1

        # Representation of screws currently loaded in storage bay
        self.GREENSCREW = 1
        self.REDSREW = 2
        self.YELLOWSCREW = 3
        self.BLUESCREW = 4
        
        self.EMPTY = 0

        self.screws = []

        
        self.lift_position = self.DOWN # Default lift position



    # Move storage up or down
    # Direction accepts Storage.UP or Storage.DOWN
    def lift(self, direction, speed=70, rotations=3): 

        if not direction:
            speed = -speed
    
        self.Lift.on_for_rotations(SpeedPercent(speed), rotations)

        # TODO: Handle idiotizm
        self.lift_position = -self.lift_position
   
    # Rotate storage
    # direction accepts Storage.GOODDIRECTION or Storage.BADDIRECTION
    def rotate(self, rotations=1, step=90, speed=SpeedPercent(25), direction=1):
        
        if (self.lift_position == self.DOWN) and step==90:
            self.screws.rotate(rotations * direction)

        if not direction:
            speed = -speed

        self.Rotor.on_for_degrees(speed, step*rotations)

    # loads screws to storage bay
    def load_screws(self):
        self.lift(self.DOWN)

        # #########
        #   3 # 0 #
        # #########
        # # 2 # 1 
        # #   #####

        self.screws = [
            self.GREENSCREW,
            self.REDSREW,
            self.YELLOWSCREW,
            self.BLUESCREW
        ]

    # unloads a singular screw
    def unload_screw(self, screw):
        index = self.screws.index(screw)

        if index == 0:
            self.lift(self.UP)
            self.rotate()
            self.lift(self.DOWN)
            self.rotate(rotations=4)
            # TODO: back up
            self.rotate(rotations=3)
        else:
            self.rotate(rotations=index)
            # TODO: back up
            self.rotate(rotations=(4 - index))

        self.screws[index] = self.EMPTY

            
        
