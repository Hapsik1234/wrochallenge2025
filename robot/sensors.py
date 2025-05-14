
from ev3dev2.sensor import INPUT_1, INPUT_2                                                  # type: ignore
from ev3dev2.sensor.lego import ColorSensor                                         # type: ignore
                                              

class Sensors:

      def __init__(self,clSensor_portLeft = INPUT_1,clSensor_portRight = INPUT_2):
            self.clSensRight = ColorSensor(clSensor_portRight)
            self.clSensLeft = ColorSensor(clSensor_portLeft)

      def Sensing(self):
        self.clSensRight.mode = 'COL-COLOR'    
        self.clSensLeft.mode = 'COL-COLOR'
        
        if self.clSensLeft.color == 12
            

    

    