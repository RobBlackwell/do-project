#!/usr/bin/env python
import serial
import sys

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)

# turn on the LEDs
#ser.write("L1\r".encode('UTF-8'))
#ser.write("L1\r")
ser.write("STATUS\r")

ser.write("I\r")
ser.write("C,1\r")

line = ""

while True:
  data = ser.read()
  if(data == "\r"):
    print "Received from sensor:" + line
    line = ""
  else:
    line = line + data
