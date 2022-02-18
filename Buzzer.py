#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
Pin=3
GPIO.setup(Pin, GPIO.OUT)
p = GPIO.PWM(Pin, 4000)

try:
    while True:
        p.start(100)
        time.sleep(1)
        p.stop()
        time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()