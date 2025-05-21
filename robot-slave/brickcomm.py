import rpyc # type: ignore
from time import sleep


def yes():

    conn = rpyc.classic.connect('192.168.0.1')
    # import ev3dev2 on the remote ev3dev device
    ev3dev2_motor = conn.modules['ev3dev2.motor']
    ev3dev2_sensor = conn.modules['ev3dev2.sensor']
    ev3dev2_sensor_lego = conn.modules['ev3dev2.sensor.lego']

    # Use the LargeMotor and TouchSensor on the remote ev3dev device
    motor = ev3dev2_motor.MediumMotor(ev3dev2_motor.OUTPUT_A)

    # If the TouchSensor is pressed, run the motor
    motor.run_timed(time_sp=1000, speed_sp=600)

if __name__ == '__main__':
    yes()