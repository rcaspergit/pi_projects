import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


address_pins = [3,5,29,8,10,11,12,13,15,16,18,19,21,22,23]

write_enable = 24
output_enable = 26
#chip_enable = 29

data_pins = [31,32,33,35,36,37,38,40]


GPIO.setup(write_enable,GPIO.OUT,initial=1)
GPIO.setup(output_enable,GPIO.OUT, initial=1)
#GPIO.setup(chip_enable,GPIO.OUT, initial=0)


def set_data(outbyte):
    for i in range(len(data_pins)):
        GPIO.output(data_pins[i],0)
    return 

for y in  range(len(address_pins)):
    GPIO.setup(address_pins[y], GPIO.OUT, initial=0)

for y in range(len(data_pins)):
    GPIO.setup(data_pins[y], GPIO.OUT, initial=0)

try:
     for x in range(0x8000):
        for y in range(len(address_pins)):
            GPIO.output(address_pins[y],((x>>y)&1))
        set_data(0x00)
        sleep(.0001)
        GPIO.output(write_enable,0)
        sleep(.00001)
        GPIO.output(write_enable,1)
        sleep(.012)

except:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
