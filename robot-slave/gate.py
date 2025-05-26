from ev3dev2.motor import LargeMotor, OUTPUT_D # type: ignore


class Gate:
    def __init__(self, motor):
        self.gate_motor = motor
        self.UP = 1
        self.DOWN = -1
    
    def rotate_gate(self, direction, step = 90, speed = 80):
        self.gate_motor.on_for_degrees(speed * direction, step)
