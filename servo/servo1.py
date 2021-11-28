import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)  # note. pin 11 will output 50hz pulse

servo1.start(0)
time.sleep(2)

duty = 2

while duty <=12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    
time.sleep(2)

print ("turning back 90 degrees")
servo1.ChangeDutyCycle(7)
time.sleep(1)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()
