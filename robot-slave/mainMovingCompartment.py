from ev3dev2.motor import LargeMotor, SpeedPercent   #type: ignore
from arduinocomm import *
import math

class mainCompartment:
  
  def __init__(self, Motor_portRight, Motor_portLeft):
    self.MotorRight = LargeMotor(Motor_portRight)
    self.MotorLeft = LargeMotor(Motor_portLeft)
    self.FORWARD = 1
    self.BACKWARD = -1
    self.RIGHT = 1
    self.LEFT = -1

    def orientation(self):
      
      self.sin = self.xSinus/distance1
      self.angle = math.asin(self.sin)
      self.degrees = math.degrees(self.angle)

    
      
  def MoveStraight(self, lidar1distance , lidar2distance, direction, rotations, speed = 100):
    if distance1- lidar1distance > 40:
      if distance2 - lidar2distance  > 40:
          self.MotorLeft.on_for_rotations(SpeedPercent(speed * direction), rotations)
          self.MotorRight.on_for_rotations(SpeedPercent(speed * direction), rotations)

  def Turning(self,lidar1distance,lidar2distance, turning_direction, rotations, speed=100):
   self.xSinus = distance1
   if distance1- lidar1distance > 40:
      if distance2 - lidar2distance  > 40:
      
        self.MotorLeft.on_for_rotations(SpeedPercent(speed * turning_direction), rotations)
        self.MotorRight.on_for_rotations(SpeedPercent(speed * -turning_direction), rotations)
  
        