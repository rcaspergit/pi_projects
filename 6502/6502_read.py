import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
import pdb


# Address_pins = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24]
Address_pins = [24,23,22,21,19,18,16,15,13,12,11,10,8,7,5,3]
Data_pins = [26,29,31,32,33,35,36,37]

clock_pin = 38
wrb = 40

for index in  range(len(Address_pins)):
    GPIO.setup(Address_pins[index], GPIO.IN)

for index in range(len(Data_pins)):
    GPIO.setup(Data_pins[index], GPIO.IN)

GPIO.setup(clock_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(wrb,GPIO.IN)

while(True):
    GPIO.wait_for_edge(clock_pin,GPIO.RISING)
    bus_addr = 0
    for y in range(len(Address_pins)):
        bus_addr = (bus_addr <<1) + GPIO.input(Address_pins[y])
    data = 0
    for i in range(len(Data_pins)):
        data = (data << 1) + GPIO.input(Data_pins[i])
    rwb = GPIO.input(40)

    print("address " + hex(bus_addr) +
          "  data " + hex(data) +
          "  WRB " + hex(rwb) )


