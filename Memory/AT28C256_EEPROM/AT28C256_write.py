import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


address_pins = [3,5,29,8,10,11,12,13,15,16,18,19,21,22,23]
# address_pins = [23,22,21,19,18,16,15,13,,12,11,10,8,29,5,3]

write_enable = 24
output_enable = 26
#chip_enable = 29

data_pins = [31,32,33,35,36,37,38,40]
# data_pins = [31,32,33,35,36,37,38,40]

low_bytes = [   0xa9, 0x81, 0x8d, 0x00, 0x60,
                0xa9, 0x42, 0x8d, 0x00, 0x60,
                0xa9, 0x24, 0x8d, 0x00, 0x60,
                0xa9, 0x18, 0x8d, 0x00, 0x60,
                0x4c, 0x00, 0x00]

high_bytes = [0x00,0x80]
high_byte_addresses = [0x7ffc,0x7ffd]

GPIO.setup(write_enable,GPIO.OUT,initial=1)
GPIO.setup(output_enable,GPIO.OUT, initial=1)
#GPIO.setup(chip_enable,GPIO.OUT, initial=0)


def set_data(outbyte):
#    print("outbyte = " + hex(outbyte))
    for i in range(len(data_pins)):
        GPIO.output(data_pins[i],(outbyte>>i)&1)
    return 

for y in  range(len(address_pins)):
    GPIO.setup(address_pins[y], GPIO.OUT, initial=0)

for y in range(len(data_pins)):
    GPIO.setup(data_pins[y], GPIO.OUT, initial=0)

try:
     for x in range(len(low_bytes)):
        for y in range(len(address_pins)):
            GPIO.output(address_pins[y],((x>>y)&1))
        set_data(low_bytes[x])
        sleep(.0001)
        GPIO.output(write_enable,0)
        sleep(.01)
        GPIO.output(write_enable,1)

     for x in range(len(high_bytes)):
        for y in range(len(address_pins)):
            GPIO.output(address_pins[y],((high_byte_addresses[x]>>y)&1))
#        print("address to write " + hex( high_byte_addresses[x]))
        set_data(high_bytes[x])
        sleep(.0001)
        GPIO.output(write_enable,0)
        sleep(.01)
        GPIO.output(write_enable,1)
        sleep(.001)


except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
