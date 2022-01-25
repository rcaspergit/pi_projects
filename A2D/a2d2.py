#! /usr/bin/python3
# Pcf8591.py file
import smbus
import time
bus = smbus.SMBus (1)
address = 0x48

def read (control):
  write = bus.write_byte_data (address, control, 0)
  read = bus.read_byte (address)
  return read


def write(val):
 try:
   temp = val # move string value to temp
   temp = int(temp) # change string to integer
 # print temp to see on terminal else comment out
   bus.write_byte_data(address, 0x40, temp)
 except Exception as  e:
   print("Error: Device address: 0x%2X" % address)
   print(e)

while True:
  poti = read (0x40)
  light = read (0x41)
  temp = read (0x42)
  ain2 = read (0x43)
  print ("temperature:", temp, "light:", light,"Voltage - Poti:", poti)
  write(poti)
  time. sleep (0.5)
  
