

from ev3dev2.motor import LargeMotor, OUTPUT_D # type: ignore


class Gate:
    def __init__(self,GateRotor_port = OUTPUT_D):
        self.GateRotor = LargeMotor(GateRotor_port)
        self.UP = 1
        self.DOWN = -1
    
    def RotateGate(self,direction,step = 90, speed = 80):
        self.GateRotor.on_for_degrees(speed * direction, step)
