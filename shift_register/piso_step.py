import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
import pdb

GPIO.setwarnings(False)

Latch = 33
Clock = 35
Data = 37

count = 0

GPIO.setup(Latch,GPIO.OUT,initial=0)
GPIO.setup(Data,GPIO.IN)
GPIO.setup(Clock,GPIO.OUT,initial=0)


# pdb.set_trace()
try:
     while (True):
        var = input("step")
        if (count %8 == 0):
            GPIO.output(Latch,1)
            sleep(0.1)
            GPIO.output(Clock,1)
            sleep(0.1)
            GPIO.output(Clock,0)
            GPIO.output(Latch,0)
            print("strobed latch")
        bit = GPIO.input(Data)
        print("data = " + str(bit) + " count = " + str(count % 8))
        GPIO.output(Clock,1)
        sleep(0.1)
        GPIO.output(Clock,0)
        count += 1

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   

GPIO.cleanup()          
