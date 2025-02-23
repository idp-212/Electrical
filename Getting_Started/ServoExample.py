from machine import Pin, PWM
from time import sleep

# Orange -- pin 1: link to PICO pin 13 channel 1 and to PICO pin 15 for channel 2
# Red -- pin 2
# Brown -- pin 3


# Set up PWM Pin for servo control
servo_pin = machine.Pin(15)
servo = PWM(servo_pin)

# Set duty cycle for different angles
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

# Set PWM frequency
frequency = 50
servo.freq(frequency)
try:
    while True:
        # Servo at 0 degrees
        servo.duty_u16(min_duty)
        sleep(2)
        
        # Servo at 0 degrees
        servo.duty_u16(half_duty)
        sleep(2)
        
        # Servo at 0 degrees
        servo.duty_u16(max_duty)
        sleep(2)
except KeyboardInterrupt:
    print("Keyboard interrupt")
    #Turn off PWM
    servo.deinit()
        
        
        
        
        
        
        
        