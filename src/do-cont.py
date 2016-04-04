#!/usr/bin/env python
import serial
import sys

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)

ser.write("C,1\r")
line = ""

while True:
  data = ser.read()
  if(data == "\r"):
    print(line)
    line = ""
  else:
    line = line + data
