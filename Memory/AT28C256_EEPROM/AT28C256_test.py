import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


GPIO.cleanup()

address_pins = [3,5,29,8,10,11,12,13,15,16,18,19,21,22,23]
#address_pins = [23,22,21,19,18,16,15,13,12,11,10,8,7,5,3]

write_enable = 24
output_enable = 26
# chip_enable = 29

data_pins = [31,32,33,35,36,37,38,40]


GPIO.setup(write_enable,GPIO.OUT,initial=1)
GPIO.setup(output_enable,GPIO.OUT, initial=1)
# GPIO.setup(chip_enable,GPIO.OUT, initial=0)

for y in  range(len(address_pins)):
    GPIO.setup(address_pins[y], GPIO.OUT, initial=0)

for y in range(len(data_pins)):
    GPIO.setup(data_pins[y], GPIO.OUT, initial=0)


try:    

   for i in range(len(address_pins)):
       dummy = input("ready to light up " + str(i) + "th addr bit on GPIO " + str(address_pins[i]))
       GPIO.output(address_pins[i],1)
   
   for i in range(len(data_pins)):
       dummy = input("ready to light up " + str(i) + "th data bit on GPIO " + str(data_pins[i]))
       GPIO.output(data_pins[i],1)


except:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
