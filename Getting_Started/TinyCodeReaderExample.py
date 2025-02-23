import network
import struct # Module converts between python values and C structs represented as Python bytes objects
from time import sleep
import machine

# INCORRECT CONNECTIONS WILL DESTROY THE SENSOR, CHECK WITH MULTIMETER BEFORE POWER/USE
# Red -- 3v3
# Black -- gnd
# Blue -- sda
# Yellow -- scl

# I2C ID/address of decimal 12
TINY_CODE_READER_I2C_ADDRESS = 0x0C

# Pause time between sensor polls
TINY_CODE_READER_DELAY = 0.05

# Bunch of configurations
TINY_CODE_READER_LENGTH_OFFSET = 0
TINY_CODE_READER_LENGTH_FORMAT = "H"
TINY_CODE_READER_MESSAGE_OFFSET = TINY_CODE_READER_LENGTH_OFFSET +
struct.calcsize(TINY_CODE_READER_LENGTH_FORMAT)
TINY_CODE_READER_MESSAGE_SIZE = 254
TINY_CODE_READER_MESSAGE_FORMAT = "B" * TINY_CODE_READER_MESSAGE_SIZE
TINY_CODE_READER_I2C_FORMAT = TINY_CODE_READER_LENGTH_FORMAT +
TINY_CODE_READER_MESSAGE_FORMAT
TINY_CODE_READER_I2C_BYTE_COUNT = struct.calcsize(TINY_CODE_READER_I2C_FORMAT)

# Set up for the Pico
# pin 19 is yellow, pin 18 is blue
i2c = machine.I2C(1, scl=machine.Pin(19), sda=machine.Pin(18), freq=400000)

print(i2c.scan())

while True:
    sleep(TINY_CODE_READER_DELAY)
    read_data = i2c.readfrom(TINY_CODE_READER_I2C_ADDRESS, TINY_CODE_READER_I2C_BYTE_COUNT)
    
    print("raw data", read_data)
    
    message_length, = struct.unpack_from(TINY_CODE_READER_LENGTH_FORMAT, read_data, TINY_CODE_READER_LENGTH_OFFSET)
    message_bytes = struct.unpack_from(TINY_CODE_READER_MESSAGE_FORMAT, read_data, TINY_CODE_READER_MESSAGE_OFFSET)
    
    if message_length == 0:
        print("Nothing")
        continue
    try:
        message_string = bytearray(message_bytes[0:message_length]).decode("utf-8")
        print("barcode:", message_string)
    except:
        print("Couldn't decode as UTF 8")
        pass

