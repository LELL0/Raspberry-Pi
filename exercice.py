i = 0
while True :
     i = i + 1
     if i == 6 :       
         break
        
     flag=0
     try:
         x = int(input("enter the number 8:" ))
         flag=0
     except:
         print("enter an integer: ")
         flag=1
         
     while flag==1:
         try:
             x = int(input("enter the number 8:" ))
             flag=0
         except:
              print("enter an integer: ")
              flag=1
              
#      if x > 8 :
#             print ("za8ir l ra2em lol")
#      elif x < 8 :
#             print ("kabir l ra2em lol")
#      else:
#          print("Bravo")
         

    
     if x > 8 or x < 8  :
            print ("Wrong Input")
     else:
         print("Bravo")
         
     y = float(input("enter the number 8.5:" ))

     if y > 8.5 :
         print("za8ir l ra2em")
     elif y < 8.5 :
         print ("kabir l ra2em")
                    
     else:
         print("Bravo")
    
    
        

  
         
        

   
