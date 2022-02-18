
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT) #green
GPIO.setup(13,GPIO.OUT) #red
GPIO.setup(16,GPIO.OUT) #yellow
 
 trigger=40
 echo=38
 
 GPIO.setup(echo,GPIO.IN) #sensor IN
 GPIO.setup(trigger,GPIO.OUT) #sensor OUT
 
 while True:
     time.sleep(0.5)
     GPIO.output(trigger,True)
     time.sleep(0.0001)
     GPIO.output(trigger,False)
     while GPIO.input(echo)==0:
         pulseStart = time.time()
     while GPIO.input(echo)==1:
         pulseEnd = time.time()
     pulseDuration = pulseEnd - pulseStart
     distance = pulseDuration * 17150
     print("distance: ",distance)
     time.sleep(2)    
   
    
    
    
    
    
    

steven=float(input("enter sleep delay: "))


sleven=int(input("enter sleven delay: "))
 
for i in range(0,sleven):
     
    GPIO.output(13,True)
    print("DAW AHMAR")
    time.sleep(steven)
    time.sleep(0.1)
    GPIO.output(16,False)
     
    GPIO.output(15,True)
    print("DAW AKHDAR")
    time.sleep(0.1)
    GPIO.output(13,False)
     
    GPIO.output(16,True)
    print("DAW ASFAR")
    time.sleep(steven)
    time.sleep(0.1)
    GPIO.output(15,False)

 
      