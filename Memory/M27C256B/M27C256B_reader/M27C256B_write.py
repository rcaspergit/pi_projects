import RPi.GPIO as GPIO            # import RPi.GPIO module  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
from time import sleep

Ai = [11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
Bi = [3,5,7,8,10,19,21,23]


ChipEnable = 26
WriteEnable = 24

GPIO.setup(ChipEnable,GPIO.OUT, initial=1)
GPIO.setup(WriteEnable,GPIO.OUT, initial=1)

for y in range(len(Bi)):
    GPIO.setup(Bi[y],GPIO.OUT,initial=0)

for y in  range(len(Ai)):
    GPIO.setup(Ai[y], GPIO.OUT, initial=0)

try:
     for x in range(0x0,0xff):
        for y in range(15):
            GPIO.output(Ai[y],((x>>y)&1))
        for y in range(8):
            GPIO.output(Bi[y],((x>>y)&1))
        for i in range(10):
            GPIO.output(ChipEnable,0)
            GPIO.output(ChipEnable,1)
#        print("pass number " + str(x))
#        sleep(0.2)

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   

GPIO.cleanup()          
