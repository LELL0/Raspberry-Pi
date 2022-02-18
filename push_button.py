import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led32 = 32
Switch = 37
h=1

GPIO.setup(led32,GPIO.OUT) 
GPIO.setup(Switch,GPIO.IN) 

def open_file():
        f=open("gyl.txt","w")
        f.write(text)
        f.close()

# def initiating():   
#     f = open("gyl.txt","r")
#     sleven = bool(f.read())
#     f.close()

# x=int(input("1 to initiating \n2 to continue the loop: \n press 0 to exit\n"))
# 
# while(x!=0):
#     if x==1:
#         initiating()
#         GPIO.output(led32, sleven)
#     
#     elif(x==2):
    
# initiating()

i = 0

f = open("gyl.txt","r")
sleven = bool(f.read())
f.close()
GPIO.output(led32, sleven)

# time.sleep(5)

while True:
        button_state = GPIO.input(Switch)
        while button_state == True:
           if h==0:
              var = GPIO.input(led32)
             
              if var == True:
                  text="0"
                  GPIO.output(led32, False)
                  open_file()
              else:
                  text="1"
                  GPIO.output(led32, True)
                  open_file()
           h=1
           button_state = GPIO.input(Switch)
           time.sleep(0.001)
        h=0
#     x=int(input("1 to initiating \n2 to continue the loop \n press 0 to exit: \n"))

# f = open("gyl.txt","r")
# sleven = f.readline()
# print(sleven)
# f.close()

#         f=open("gyl.txt","w")
#         f.write(text)

# button_state = GPIO.input(Switch)
# while button_state == False:
#     if button_state == True:
#         var = GPIO.input(led32)
#         if var == 1:
#             GPIO.output(led32, False)
#         else:
#             GPIO.output(led32, True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#      time.sleep(1)
#      button_state = GPIO.input(Switch)
#          
#      if button_state == True:
#             var = GPIO.input(led32)
#              
#             if var == 1:
#                GPIO.output(led32, False)
#             else:
#                GPIO.output(led32, True)
#                print('Button Pressed...')
#         
#         time.sleep(0.2)
#         GPIO.output(led32, False)
 #        print('Button  Not     Pressed...')
#     print(GPIO.input(Switch))
 #    if (flag1==flag2):
#         GPIO.output(led32, flag_led)
#         flag_led=not flag_led
#           var = GPIO.input(led32)
#           if var == 1:
#               GPIO.output(led32, False)
#           else:
#               GPIO.output(led32, True)
# while button_state
#    if button_state == False:
#         var = GPIO.input(led32)
#         if var == 1:
#             GPIO.output(led32, False)
#         else:
#             GPIO.output(led32, True)
# 
