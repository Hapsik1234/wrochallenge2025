from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_D, OUTPUT_C   #type: ignore
from arduinocomm import *
import math

class main_compartment:
  
  def __init__(self, Motor_portRight=OUTPUT_D, Motor_portLeft=OUTPUT_C):
    self.MotorRight = LargeMotor(Motor_portRight)
    self.MotorLeft = LargeMotor(Motor_portLeft)
    self.FORWARD = -1
    self.BACKWARDS = -self.FORWARD
    self.RIGHT = 1
    self.LEFT = -1

    def orientation(self):
      
      self.sin = self.xSinus/distance_right # zawsze 1? # dlaczego to jest parametr?
      self.angle = math.asin(self.sin) 
      self.degrees = math.degrees(self.angle) 

    
      
  def move_straight(self, lidar1distance , lidar2distance, direction, rotations, off = 40, speed = 100):
    '''
    :param int lidar1distance: plug in lidar 1
    :param int lidar2distance: plug in lidar 2
    :param int direction: direction, accepts m.FORWARD and m.BACKWARDS
    :param float rotations: number of rotations for the motors to perform
    :param int off: measurement error
    :param int speed: motor speed (percentage)
    theoretically should go in a straight line
    '''
    # if lidar1distance >= distance_right:
    #   if lidar1distance > distance_right + off:
    # elif lidar1distance < distance_right + off
    #    if lidar2distance >= distance_left :
    #      if lidar2distance > distance_left + off:
    #    elif lidar2distance < distance_left + off: 
    self.MotorLeft.on_for_rotations(SpeedPercent(speed * direction), rotations, block=False)
    self.MotorRight.on_for_rotations(SpeedPercent(speed * direction), rotations)

  def turning(self,lidar1distance,lidar2distance, turning_direction, rotations, speed=100):
   self.xSinus = distance_right
   if lidar1distance > 40:
      if lidar2distance  > 40:
        self.MotorLeft.on_for_rotations(SpeedPercent(speed * turning_direction), rotations)
        self.MotorRight.on_for_rotations(SpeedPercent(speed * -turning_direction), rotations)


