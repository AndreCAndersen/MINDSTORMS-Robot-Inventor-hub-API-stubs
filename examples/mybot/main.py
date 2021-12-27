from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_a = Motor('A')
motor_b = Motor('B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')
# Initialize the Distance Sensor connected to Port D.
distance_sensor = DistanceSensor('D')

distance_sensor.light_up_all()
motor_a.start()
wait_for_seconds(2)
distance_sensor.wait_for_distance_closer_than(10, 'cm')
motor_a.stop()
