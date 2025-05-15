from ev3dev2.motor import LargeMotor, SpeedPercent   #type: ignore

class mainCompartment:
    def __init__(self,Motor_portRight,Motor_portLeft):
        self.MotorRight = LargeMotor(Motor_portRight)
        self.MotorLeft = LargeMotor(Motor_portLeft)
        self.FORWARD = 1
        self.BACKWARD = -1
        self.RIGHT = 1
        self.LEFT = -1
        
    def MoveStraight(self, direction, rotations, speed = 100):
        self.MotorLeft.on_for_rotations(SpeedPercent(speed * direction), rotations)
        self.MotorRight.on_for_rotations(SpeedPercent(speed * direction), rotations)

    def Turning(self, turning_direction, rotations, speed=100):
        self.MotorLeft.on_for_rotations(SpeedPercent(speed * turning_direction), rotations)
        self.MotorRight.on_for_rotations(SpeedPercent(speed * -turning_direction), rotations)

        