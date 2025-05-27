from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_D, OUTPUT_C   #type: ignore
from arduinocomm import *
import math

# Manual python console import
# from arduinocomm import *; from mainMovingCompartment import *; m = main_compartment(); from storage import *; s = Storage(m)


class main_compartment:
  
  def __init__(self, Motor_portRight=OUTPUT_D, Motor_portLeft=OUTPUT_C):
    self.MotorRight = LargeMotor(Motor_portRight)
    self.MotorLeft = LargeMotor(Motor_portLeft)
    self.FORWARD = -1
    self.BACKWARDS = -self.FORWARD
    self.RIGHT = 2
    self.LEFT = -2

  def orientation(self):
    
    sin = self.xSinus/sensor_readings.distance_left
    angle = math.asin(sin) 
    self.degrees = math.degrees(angle) 

    
      
  def move_to(self, exptected_ldistance, off = 200, speed = 100):
    '''
    :param int exptected_ldistance: exptected distance from wall 1
    :param int lidar2distance: exptected distance from wall 2
    :param int direction: direction, accepts m.FORWARD and m.BACKWARDS
    :param float rotations: number of rotations for the motors to perform
    :param int off: measurement error
    :param int speed: motor speed (percentage)
    theoretically should go somewhere
    '''
    # if exptected_ldistance >= distance_right:
    #   if exptected_ldistance > distance_right + off:
    # elif exptected_ldistance < distance_right + off
    #    if lidar2distance >= distance_left :
    #      if lidar2distance > distance_left + off:
    #    elif lidar2distance < distance_left + off: 
    while abs(exptected_ldistance - sensor_readings.distance_right) >= off:
        if exptected_ldistance >= sensor_readings.distance_right:
          direction = self.FORWARD
        else:
          direction = self.BACKWARDS
      #   if lidar2distance >= distance_left:
      #    direction = self.RIGHT
      #  else:
      #    direction = self.LEFT
        # print("distance_right: " + str(sensor_readings.distance_right) + "expected_ldistance: " + str(exptected_ldistance) + "distance from to: " + str(abs(exptected_ldistance - sensor_readings.distance_right)))
        self.move_straight(direction, 0.5, 100)
        
   
  def move_straight(self, direction, rotations, speed, coast=False):
    self.MotorLeft.on_for_rotations(SpeedPercent(speed * direction), rotations, block=False, brake=False)
    self.MotorRight.on_for_rotations(SpeedPercent(speed * direction), rotations, brake=False)

  def turning(self,exptected_angle, turning_direction, rotations, speed):
   self.xSinus = sensor_readings.distance_left
   while abs(exptected_angle - self.degrees) > 5:
        if exptected_angle > self.degrees :
          turning_direction = self.LEFT
        else:
          turning_direction = self.RIGHT
        self.orientation()
        self.MotorLeft.on_for_rotations(SpeedPercent(speed * turning_direction / 2), rotations, block=False)
        self.MotorRight.on_for_rotations(SpeedPercent(speed * -turning_direction / 2), rotations)


