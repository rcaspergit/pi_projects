import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

led_pin = 18

pwm_led = GPIO.PWM(led_pin,500)
pwm_led.start(100)

try:
    while True:
        duty_s = input("enter brightnes(0 to 100):")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)

except KeyboardInterrupt:
    print("keyboard kill")

finally:
    GPIO.cleanup()


