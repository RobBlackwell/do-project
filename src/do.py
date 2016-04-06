#!/usr/bin/env python3
import serial

usbport = '/dev/ttyAMA0'

SER=""

def connect ():
    global SER
    SER = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)
    
def receive(ser=None):
    if ser is None:
        ser = SER
    line = ""
    while True:
        data = ser.read().decode('utf-8')
        if(data == "\r"):
            return(line)
        else:
            line = line + data
      
def send(s, ser=None):
    if ser is None:
        ser = SER
    ser.write(bytes(s,'utf-8'))


