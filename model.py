import cv2
from collections import Counter
from module3a import findnameoflandmark,findpostion
import math
import requests

cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
while True:
     ret, frame = cap.read() 
     #Unedit the below line if your live feed is produced upsidedown
     #flipped = cv2.flip(frame, flipCode = -1)
    
     frame1 = cv2.resize(frame, (640, 480))
     a = findpostion(frame1)
     b = findnameoflandmark(frame1)
     

     if len(b and a)!=0:
        finger = []
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
           #print (b[4])
          
        else:
           finger.append(0)   
        
        fingers=[] 
        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               #print("which fing: " + b[tipname[id]])

               fingers.append(1)
    
            else:
               fingers.append(0)
    
     #print(fingers)
     #dec = fingers[0] + fingers[1] + fingers[2] + fingers[3]
     x = fingers + finger
     c = Counter(x)
     up = c[1]
     down = c[0]
     if up == 5 and down == 0:
        m = "5"
     elif up == 1 and down == 4:
        m = "1"
        print("1 finger is up.")
     elif up == 2 and down == 3:
        m = "2"
        print("2 fingers are up.")
     elif up == 3 and down == 2:
        m = "3"
        print("3 fingers are up.")
     elif up == 4 and down == 1:
        m = "4"
        print("4 fingers are up.")
     else:
        m = "0"
        print("No finger is up.") 
  
    #print('This many fingers are up - ', up)
    #print('This many fingers are down - ', down)
     requests.get("http://blr1.blynk.cloud/external/api/update?token=UyCQT6zof3Ll3YCZ6JB5ucniV5bP0aqs&v0=" + m)
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     
    
     #if key == ord("q"):
        #speak("you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
     
     if key == ord("s"):
         break