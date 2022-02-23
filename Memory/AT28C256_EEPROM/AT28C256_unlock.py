import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


# address_pins = [3,5,29,8,10,11,12,13,15,16,18,19,21,22,23]
address_pins = [23,22,21,19,18,16,15,13,12,11,10,8,29,5,3]

write_enable = 24
output_enable = 26
#chip_enable = 29

data_pins = [31,32,33,35,36,37,38,40]


GPIO.setup(write_enable,GPIO.OUT,initial=1)
GPIO.setup(output_enable,GPIO.OUT, initial=1)
#GPIO.setup(chip_enable,GPIO.OUT, initial=0)

for y in  range(len(address_pins)):
    GPIO.setup(address_pins[y], GPIO.OUT, initial=0)

for y in range(len(data_pins)):
    GPIO.setup(data_pins[y], GPIO.OUT, initial=0)


def set_addr_5s():
    GPIO.output(23,1)
    GPIO.output(22,0)
    GPIO.output(21,1)
    GPIO.output(19,0)
    GPIO.output(18,1)
    GPIO.output(16,0)
    GPIO.output(15,1)
    GPIO.output(13,0)
    GPIO.output(12,1)
    GPIO.output(11,0)
    GPIO.output(10,1)
    GPIO.output(8,0)
    GPIO.output(29,1)
    GPIO.output(5,0)
    GPIO.output(3,1)

def set_addr_2as():
    GPIO.output(23,0)
    GPIO.output(22,1)
    GPIO.output(21,0)
    GPIO.output(19,1)
    GPIO.output(18,0)
    GPIO.output(16,1)
    GPIO.output(15,0)
    GPIO.output(13,1)
    GPIO.output(12,0)
    GPIO.output(11,1)
    GPIO.output(10,0)
    GPIO.output(8,1)
    GPIO.output(29,0)
    GPIO.output(5,1)
    GPIO.output(3,0)

def set_data_AA():
    GPIO.output(40,1)
    GPIO.output(38,0)
    GPIO.output(37,1)
    GPIO.output(36,0)
    GPIO.output(35,1)
    GPIO.output(33,0)
    GPIO.output(32,1)
    GPIO.output(31,0)

def set_data_55():
    GPIO.output(40,0)
    GPIO.output(38,1)
    GPIO.output(37,0)
    GPIO.output(36,1)
    GPIO.output(35,0)
    GPIO.output(33,1)
    GPIO.output(32,0)
    GPIO.output(31,1)

def set_data_80():
    GPIO.output(40,1)
    GPIO.output(38,0)
    GPIO.output(37,0)
    GPIO.output(36,0)
    GPIO.output(35,0)
    GPIO.output(33,0)
    GPIO.output(32,0)
    GPIO.output(31,0)

def set_data_20():
    GPIO.output(40,0)
    GPIO.output(38,0)
    GPIO.output(37,1)
    GPIO.output(36,0)
    GPIO.output(35,0)
    GPIO.output(33,0)
    GPIO.output(32,0)
    GPIO.output(31,0)


dummy = 12

try:    
   set_addr_5s() 
   set_data_AA()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)
#   sleep(5)
   set_addr_2as()
   set_data_55()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)
#   sleep(5)
   set_addr_5s() 
   set_data_80()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)
#   sleep(5)
   set_addr_5s() 
   set_data_AA()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)
#   sleep(5)
   set_addr_2as() 
   set_data_55()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)
#   sleep(5)
   set_addr_5s() 
   set_data_20()
   dummy=dummy*5
   GPIO.output(write_enable,0)
   dummy=dummy*5
   GPIO.output(write_enable,1)

   sleep(.001)

except:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
