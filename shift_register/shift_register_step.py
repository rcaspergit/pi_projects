import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
import pdb

GPIO.setwarnings(False)

Strobe = 11
Data = 13
Clock = 15

GPIO.setup(Strobe,GPIO.OUT,initial=0)
GPIO.setup(Data,GPIO.OUT,initial=0)
GPIO.setup(Clock,GPIO.OUT,initial=0)


# pdb.set_trace()
try:
     for x in range(0x0,0x100):
        for y in range(8):
            GPIO.output(Data,((x>>y)&1))
            GPIO.output(Strobe,1)
            GPIO.output(Clock,1)
            GPIO.output(Clock,0)
            GPIO.output(Strobe,0)
        sleep(.2)
          
#        sleep(2)

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   

GPIO.cleanup()          
