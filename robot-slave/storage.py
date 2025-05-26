#!/usr/bin/env python3
import math
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent              # type: ignore
from ev3dev2.motor import MediumMotor as SmallMotor                                 # type: ignore
from mainMovingCompartment import *

def rotate(arr):
    element = arr.pop()
    arr.insert(0, element)
    return arr

class Storage:
    
    def __init__(self, main_compartment: main_compartment, rotor_port=OUTPUT_B, lift_port=OUTPUT_A):
        
        self.Rotor = SmallMotor(rotor_port) # The spinning swastika
        self.Lift = LargeMotor(lift_port) # Storage up and down motor
        self.Main_Compartment = main_compartment

        self.rotation = 0

        self.UP = 1
        self.DOWN = -1

        self.GOODDIRECTION = 1
        self.BADDRIERECTION = -1

        # Representation of screws currently loaded in storage bay
        self.GREENSCREW = 1
        self.REDSCREW = 2
        self.YELLOWSCREW = 3
        self.BLUESCREW = 4
        
        self.EMPTY = 0

        self.screws = [
            self.REDSCREW,
            self.YELLOWSCREW,
            self.BLUESCREW,
            self.GREENSCREW
            ]

        
        self.lift_position = self.DOWN # Default lift position



    # Move storage up or down
    # Direction accepts Storage.UP or Storage.DOWN
    def lift(self, direction, speed=30, degrees=180): 

        if direction < 0:
            speed = -speed
    
        self.Lift.on_for_degrees(SpeedPercent(speed), degrees, block=True)
        self.Lift.wait_until_not_moving()

        # TODO: Handle idiotism
        self.lift_position = -self.lift_position
   
    # Rotate storage
    # direction accepts Storage.GOODDIRECTION or Storage.BADDIRECTION
    def rotate(self, rotations=1, step=90, speed=SpeedPercent(10), direction=1):
        self.rotation = self.rotation + (step*rotations)

        if direction < 0:
            speed = -speed

        self.Rotor.on_for_degrees(speed, step*rotations, block=True)
        self.Rotor.wait_until_not_moving()
        
    # loads screws to storage bay
    def load_screws(self):
        self.lift(self.DOWN)

        # #########
        #   3 # 0 #
        # #########
        # # 2 # 1 
        # #   #####

        self.screws = [
            self.REDSCREW,
            self.YELLOWSCREW,
            self.BLUESCREW,
            self.GREENSCREW
        ]

    # unloads a singular screw
    def unload_screw(self, screw):
        full_changes = math.floor(self.rotation/90)
        print("rotations: "+ str(full_changes))
        screws = self.screws

        for _ in range(full_changes):
            screws = rotate(screws)
        
        index = screws.index(screw)
        print("screws: " + str(screws))
        print("index: " + str(index))

        if index == 2:
            self.lift(self.UP)
            self.rotate(1)
            self.lift(self.DOWN)
            sleep(1)
            self.screws = rotate(self.screws)
            self.rotate(2)
            self.Main_Compartment.move_straight(50, 50, self.Main_Compartment.BACKWARDS, 0.5, None, 33)
            self.rotate(1)
        elif index == 0:
            self.Main_Compartment.move_straight(50, 50, self.Main_Compartment.BACKWARDS, 0.5, None, 33)
        else:
            self.rotate(rotations=index)
            self.Main_Compartment.move_straight(50, 50, self.Main_Compartment.BACKWARDS, 0.5, None, 33)
            self.rotate(rotations=(4 - index))

        # self.screws[index] = self.EMPTY

            
    
