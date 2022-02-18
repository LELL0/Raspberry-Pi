import RPi.GPIO as GPIO
import time

desdance = -1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led1=8
led2=10
led3=11
led4=13

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)

d1=0
d2=0
d3=0
d4=0

trigger = 3
echo = 5

GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def get_distance():
    GPIO.output(trigger,0)
    time.sleep(0.5)
    GPIO.output(trigger,1)
    time.sleep(0.00001)
    
    GPIO.output(trigger,0)
    start = time.time()
    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        stop = time.time()
    elapsed = stop - start
    distance = elapsed * 17150
    return int(distance)

def getDesdance():
    global desdance,d1,d2,d3,d4
    while desdance <= 0:
        print("Plz enter a number")
        try:
            desdance = float(input("Enter the height of your water tank: "))
        except:
            print("!!! enter a valid number between 0 and <><> !!!")
    
    d1 = desdance/4
    d2 = d1*2
    d3 = d1*3
    d4 = desdance

 
def led(status1,status2,status3,status4):
    GPIO.output(led1,status1)
    GPIO.output(led2,status2)
    GPIO.output(led3,status3)
    GPIO.output(led4,status4)

getDesdance()
while True:
    distance = get_distance()
    print(distance)
    if distance <= d1:
        led(1,1,1,1)
    
    elif distance <= d2:
        led(1,1,1,0)
        
    elif distance <= d3:
        led(1,1,0,0)
         
    elif distance < d4:
        led(1,0,0,0)
    
    else:
        led(0,0,0,0)
    