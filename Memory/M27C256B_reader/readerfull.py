import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
import pdb


Ai = [11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
OutputEnable = 12
GPIO.setup(12,GPIO.OUT, initial=1)


Bi = [3,5,7,8,10,19,21,23]
#Bi = [23,21,19,10,8,7,5,3]
index = 0
for y in Bi:
    GPIO.setup(Bi[index],GPIO.IN)
    index = index + 1

dump = 0x00
outbin = open("chip.dmp", "wb")
count = 0

index = 0
for y in  Ai:
    GPIO.setup(Ai[index], GPIO.OUT, initial=0)
    index = index +1

# pdb.set_trace()
try:
     for x in range(0x0,0x7fff):
        GPIO.output(12,1)
#        sleep(2)
        for y in range(14):
            GPIO.output(Ai[y],((x>>y)&1))
        GPIO.output(12,0)
        sleep(.0001)
        for bits in range(8):
            dump = dump | (GPIO.input(Bi[bits]) << bits)
#        print(GPIO.input(Bi[2]))    
        outbin.write(dump.to_bytes(1,byteorder='little'))
        dump=0
          
#        sleep(2)

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   

GPIO.cleanup()          
