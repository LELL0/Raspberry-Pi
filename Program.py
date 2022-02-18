import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trigger = 3
echo = 5
Pin_buzzer=7
Pin_servo=11

def setup_servo():
    GPIO.setup(Pin_servo, GPIO.OUT)

def reset_servo():
    p = GPIO.PWM(Pin_servo, 50)
    p.start(0)
    
def turn_servo(angle):
    p = GPIO.PWM(Pin_servo, 50)
    duty= angle / 18 + 2
    GPIO.output(Pin_servo,True)
    p.start(duty)
    time.sleep(1)
    GPIO.output(Pin_servo,False)
    p.ChangeDutyCycle(0)
    
###################################
def setup_buzzer():
    GPIO.setup(Pin_buzzer, GPIO.OUT)

def buzz(sec):
    p = GPIO.PWM(Pin_buzzer, 4000)
    p.start(100)
    time.sleep(sec)
    p.stop()

###################################
def setup_UltraSonic():
    GPIO.setmode(GPIO.BOARD)
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
#angle 55 door is locked
#angle 150 door is open

###################################




# setup_UltraSonic()
# while True:
#     print(get_distance())

# setup_buzzer()
# buzz(0.2)

# setup_servo()
# 
# 
# while True:
#     n=float(input("inputn"))
#     turn_servo(n)