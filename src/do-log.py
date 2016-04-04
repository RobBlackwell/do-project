#!/usr/bin/env python
import serial
import sys

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)

line = ""

while True:
  data = ser.read()
  if(data == "\r"):
    print(line)
    line = ""
  else:
    line = line + data
