import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led13=36
led8=38
led40=40
led32=32
GPIO.setup(led13,GPIO.OUT) #blue
GPIO.setup(led8,GPIO.OUT) #blue
GPIO.setup(led40,GPIO.OUT) #blue
GPIO.setup(led32,GPIO.OUT) #blue

steven=float(input("enter sleep delay: "))
steven2=float(input("enter sleep2 delay: "))
 
sleven=int(input("looping: "))


def sleep(i):
    time.sleep(i)
def led(status1,status2,status3,status4):
    GPIO.output(led8,status1)
    GPIO.output(led13,status2)
    GPIO.output(led40,status3)
    GPIO.output(led32,status4)
	
for i in range(0,sleven):
    led(1,0,1,0)
    sleep(steven)
    led(0,1,0,1)
    sleep(steven2)
    led(1,0,1,0)
    
led(0,0,0,0)
	
	
	
	
