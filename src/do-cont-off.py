#!/usr/bin/env python3
import do

do.VERBOSE = True

# Connect to the Atlas Scientific DO circuit board
do.connect()
  
do.send("C,0\r")
    
ok = do.receive()
assert ok == '*OK'

