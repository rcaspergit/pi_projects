import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD


# Ai = [11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
Ai = [31,29,23,21,19,15,13,11,18,22,26,24,7,16,12,5,3,10,8]

index = 0
for y in  Ai:
    print(index,Ai[index])
    GPIO.setup(Ai[index], GPIO.OUT, initial=0)
    index = index +1

try:
    for y in range(19):
        GPIO.output(Ai[y],1)
        var = input("step " + str(y) + " address pin " + str(Ai[y]) )
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

GPIO.cleanup()
