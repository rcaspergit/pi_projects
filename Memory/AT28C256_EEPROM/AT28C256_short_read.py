import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


address_pins = [3,5,29,8,10,11,12,13,15,16,18,19,21,22,23]

write_enable = 24
output_enable = 26
# chip_enable = 29

data_pins = [31,32,33,35,36,37,38,40]



GPIO.setup(write_enable,GPIO.OUT,initial=1)
GPIO.setup(output_enable,GPIO.OUT, initial=0)
# GPIO.setup(chip_enable,GPIO.OUT, initial=0)

outfile = open("AT28C256.dmp", "wb")

def get_data():
    outbyte = 0
    for i in range(len(data_pins)):
        bit = GPIO.input(data_pins[i])
        print(str(bit))
        outbyte = outbyte | (bit << i)
        outbyte |= bit
    return outbyte


for y in  range(len(address_pins)):
    GPIO.setup(address_pins[y], GPIO.OUT, initial=0)

for y in range(len(data_pins)):
    GPIO.setup(data_pins[y], GPIO.OUT, initial=0)

try:
     for x in range(0x7ff0,0x8000):
#        var = input("stopped at " + hex(x)) 
        if ((x%0x1000) == 0):
            print("block starting at address " + hex(x))
        for y in range(len(address_pins)):
            GPIO.output(address_pins[y],((x>>y)&1))
        outbyte = get_data()
        input("address = " + hex(x))
        outfile.write(outbyte.to_bytes(1,byteorder='big'))
     outfile.close()

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
