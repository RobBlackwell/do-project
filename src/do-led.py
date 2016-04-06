#!/usr/bin/env python3
import do
import time

do.VERBOSE = True

# Connect to the Atlas Scientific DO circuit board
do.connect()

while True:
    do.send("L,1\r")
    
    ok = do.receive()
    assert ok == '*OK'

    time.sleep(2)
    do.send("L,0\r")
    
    ok = do.receive()
    assert ok == '*OK'

    time.sleep(1)


