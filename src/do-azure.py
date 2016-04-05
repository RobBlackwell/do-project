#!/usr/bin/env python3
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


def request_response(ser, s):
  ser.write(bytes(s,'utf-8'))
  line = ""
  while True:
    data = ser.read().decode('utf-8')
    if(data == "\r"):
      return(line)
    else:
      line = line + data


device = DeviceClient.DeviceClient(config.HUB, config.DEVICE_NAME, config.KEY)

device.create_sas(600)

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, serial.EIGHTBITS, serial.PARITY_NONE)

print(request_response(ser, "C,0\r"))

while True:

  r = request_response(ser, "R\r")

  msg = "{\"do\" : \"" + r + "\"" + ",\"at\" : \"" + str(datetime.now()) + "\"}"
  print(msg)
  print(device.send(bytes(msg,'utf-8')))
  time.sleep(SLEEP)

