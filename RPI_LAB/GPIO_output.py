#Python Program to demonstrate GPIO Output in Raspberry Pi
#(C)Sai Shibu
#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
#Configure GPIO Pin 17 as output
GPIO.setup(17,GPIO.OUT) 
#Set GPIO Pin to High
a=0
while a <= 5:
  GPIO.output(17,GPIO.HIGH)
#Wait for 1sec
<<<<<<< HEAD
time.sleep(2)
=======
  time.sleep(1)
>>>>>>> b66bb1791c7a9dad1d8a0e8905b5b068b1db914a
#Set GPIO Pin to Low
  GPIO.output(17,GPIO.LOW)
  time.sleep(1)
  a=a+1
