import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


Ai = [31,29,23,21,19,15,13,11,18,22,26,24,7,16,12,5,3,10,8]

Latch = 36
Clock = 38
Data = 40

GPIO.setup(Latch,GPIO.OUT,initial=0)
GPIO.setup(Data,GPIO.IN)
GPIO.setup(Clock,GPIO.OUT,initial=0)

outfile = open("w27e040.dmp", "wb")

def get_data():
    outbyte = 0
    GPIO.output(Latch,1)
#    sleep(0.01)
    GPIO.output(Clock,1)
#    sleep(0.01)
    GPIO.output(Clock,0)
    GPIO.output(Latch,0)
    for i in range(8):
        bit = GPIO.input(Data)
        outbyte = outbyte << 1
        outbyte |= bit
        GPIO.output(Clock,1)
#        sleep(0.01)
        GPIO.output(Clock,0)
    return outbyte


index = 0
for y in  Ai:
    GPIO.setup(Ai[index], GPIO.OUT, initial=0)
    index = index +1

# pdb.set_trace()
try:
     for x in range(0x0,0x7ffff):
#        var = input("stopped at " + hex(x)) 
        if ((x%0x1000) == 0):
            print("block starting at address " + hex(x))
        for y in range(19):
            GPIO.output(Ai[y],((x>>y)&1))
        outbyte = get_data()
        outfile.write(outbyte.to_bytes(1,byteorder='big'))
     outfile.close()

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
