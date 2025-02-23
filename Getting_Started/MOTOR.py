from machine import Pin, PWM

# DO NOT INSERT SCREWS MORE THAN 4 MM INTO THE MOTOR

class Motor:
    def __init__(self):
        self.m1Dir = Pin(7, Pin.OUT)	# Set motor direction
        self.pwm1 = PWM(Pin(6))			# Set speed
        self.pwm1.freq(1000)			# Set max frequency
        self.pwm1.duty_u16(0)			# Set duty cycle
    
    def off(self):
        self.pwm1.duty_u16(0)
    
    def Forward(self):
        self.m1Dir.value(0)				# forward = 0, reverse = 1, motor 1
        self.pwm1.duty_u16(int(65535*100/100)) # speed range 0 - 100, motor 1
    
    def Reverse(self):
        self.m1Dir.value(1)
        self.pwm1.duty_u16(int(65535*30/100))
