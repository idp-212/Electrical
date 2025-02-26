import time
from pinpong.board import Board
from pinpong.libs.dfrobot_urm09 import URM09 # Import the URM09 library from libs

Board("uno").begin()               # Initialization, choose the board type (uno, leonardo, xugu) and port number. If the port number is not entered, automatic recognition will be performed
#Board("uno","COM36").begin()      # Initialization with specified port on Windows
#Board("uno","/dev/ttyACM0").begin() # Initialization with specified port on Linux
#Board("uno","/dev/cu.usbmodem14101").begin()   # Initialization with specified port on Mac

urm = URM09(i2c_addr=0x11) # Initialize the sensor and set the I2C address
urm.set_mode_range(urm._MEASURE_MODE_AUTOMATIC, urm._MEASURE_RANG_500) # Set the URM09 mode to automatic detection, with a maximum measurement distance of 500cm

while True:
    dist = urm.distance_cm() # Read the distance data in centimeters (cm)
    temp = urm.temp_c() # Read the sensor temperature in Celsius (℃)

    print("Distance is %d cm         "%dist)
    print("Temperature is %.2f .c    "%temp)
    time.sleep(0.5) 