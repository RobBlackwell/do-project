#!/usr/bin/env python3
import do
import sys
import DeviceClient
import config
import time
from datetime import datetime

# Sits in a loop reading dissolved oxygen every minute from an Atlas
# Scientific probe, and sending it via the internet to a Microsoft
# Azure IOT Hub.

# Rob Blackwell <rob.blackwell@cranfield.ac.uk>

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Create a config.py with your specific Azure IOT Hub configuration:
# KEY = "xxxxx"
# HUB = "my_hub"
# DEVICE_NAME = "my_device"

SLEEP = 60

def main():

  # Connect to IOT Hub
  device = DeviceClient.DeviceClient(config.HUB, config.DEVICE_NAME, config.KEY)

  # Connect to the Atlas Scientific DO circuit board
  do.connect()
  
  do.send("C,0\r") # Continuous mode off
  ok = do.receive()
  print(ok)
  assert ok == '*OK'
  
  while True:
    
    do.send("R\r") # Request a value for DO
    
    r = do.receive()
    print(r)
    ok = do.receive()
    print(ok)
    assert ok == '*OK'
    
    msg = "{ \"deviceId\" : \"" + config.DEVICE_NAME + "\", \"do\" : \"" + r + "\"" + ", \"at\" : \"" + str(datetime.now()) + "\"}"
    print(msg)
    
    device.create_sas(600) # Shared Access Signature used for authentication
    print(device.send(bytes(msg,'utf-8')))
    
    time.sleep(SLEEP)

if __name__ == "__main__":
  main()
