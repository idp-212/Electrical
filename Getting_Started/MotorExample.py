from MOTOR import Motor
from machine import Pin
from utime import sleep

# Or linear_actuator 
motor = Motor()

while True:
    motor.Forward()
    # Extend sleep times for liner actuator to let it achieve full extension
    sleep(1)
    motor.Reverse()
    sleep(1)
    motor.off()