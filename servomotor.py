import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
Pin_servo=11
GPIO.setup(Pin_servo, GPIO.OUT)


p = GPIO.PWM(Pin_servo, 50)

p.start(2)
time.sleep(2)
p.start(7.5)
time.sleep(2)
p.start(7.5)
time.sleep(2)
p.start(12)

