#!/usr/bin/env python
import serial
import sys
import DeviceClient
import config
import time
from datetime import datetime


# START: Azure IoT Hub settings
# KEY = "xxxxx";
# HUB = "my_hub";
# DEVICE_NAME = "my_device";
# END: Azure IoT Hub settings

SLEEP = 60

device = DeviceClient.DeviceClient(config.HUB, config.DEVICE_NAME, config.KEY)

device.create_sas(600)

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)

ser.write("C,0\r")
line = ""

while True:
  ser.write("R\r")
  data = ser.read()
  if(data == "\r"):

    msg = "{\"do\" : \"" + line + "\"" + ",\"at\" : \"" + datetime.now() + "\"}"
    print(msg)
    print(device.send(msg))
    time.sleep(SLEEP)
    line = ""
    
  else:
    line = line + data
