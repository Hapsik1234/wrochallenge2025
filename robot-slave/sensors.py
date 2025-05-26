
from ev3dev2.sensor import INPUT_1, INPUT_2                                                  # type: ignore
from ev3dev2.sensor.lego import ColorSensor                                         # type: ignore
from ev3dev2.motor import MediumMotor as SmallMotor                                   # type: ignore
from ev3dev2.motor import OUTPUT_C                                              # type: ignore

class Sensors:

    def __init__(self, sens_motor, clSensor_portLeft = INPUT_1, clSensor_portRight = INPUT_2):
        self.sensRotor = sens_motor
        self.clSensRight = ColorSensor(clSensor_portRight)
        self.clSensLeft = ColorSensor(clSensor_portLeft)

        self.UP = 1
        self.DOWN = -1

      
    def sensing(self):
        self.clSensRight.mode = 'COL-COLOR'
        self.clSensLeft.mode = 'COL-COLOR'
        
    def sens_rotate(self,direction, speed = 80, step = 90):
        self.sensRotor.on_for_degrees(speed * direction, step)
    