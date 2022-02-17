import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD

Ai = [11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]

# OutputEnable = 12
# GPIO.setup(12,GPIO.OUT, initial=1)

Bi = [3,5,7,8,10,19,21,23]

for y in range(len(Bi)):
     GPIO.setup(Bi[y],GPIO.IN)
    
dump = 0x00
outbin = open("chip.dmp", "wb")
count = 0


for y in  range(len(Ai)):
    GPIO.setup(Ai[y], GPIO.OUT, initial=0)

for y in  range(15):
    GPIO.output(Ai[y], 1)
    print("bit " + str(y))
    var = input("hit key when ready for next bit")

try:
     for x in range(0x0,0x7ffff):
        for y in range(len(Ai)):
            GPIO.output(Ai[y],((x>>y)&1))
        for bits in range(8):
            dump = dump | (GPIO.input(Bi[bits]) << bits)
        outbin.write(dump.to_bytes(1,byteorder='little'))
        dump=0

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()

