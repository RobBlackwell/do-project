#!/usr/bin/env python3
import do

# Connect to the Atlas Scientific DO circuit board
do.connect()
  
do.send("STATUS\r")
    
r = do.receive()
print(r)
ok = do.receive()
print(ok)
assert ok == '*OK'


