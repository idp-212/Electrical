from time import sleep # Big module, import just the part you want
from machine import Pin

led = Pin(14, Pin.OUT)

# Or micro_switch = Pin(12, Pin.IN, Pin.PULL_UP)
# Or line_tracker = Pin(12, Pin.IN) 
button = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(button.value()) # Set LED to the push button value
    sleep(0.1)
    print(button.value()) #Value is printed to the shell screen
    

# Note button digital output is pulled high when pressed
# LED is on when digital is low
# LED is on when button is not pressed