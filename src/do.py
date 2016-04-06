#!/usr/bin/env python3
import serial

usbport = '/dev/ttyAMA0'

ser=""

def connect ():
    global ser
    ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)
    
def receive(ser=ser):
  line = ""
  while True:
    data = ser.read().decode('utf-8')
    if(data == "\r"):
      return(line)
    else:
      line = line + data
      
def send(s, ser=ser):
  ser.write(bytes(s,'utf-8'))


