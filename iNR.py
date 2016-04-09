#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### variables ##### 
import time
import numpy as np
import sys
import RPi.GPIO as GPIO
import threading 
import collections
from dateime import timedelta

f=open(~/Documents/bloodtest,'r+a')
inr = 0.0
pt = 0.0
ptnom = 0.0
isitest=0
slope=0
isiref=0
user_data_low = 0.0
user_data_high = 0.0
tester_data =0.0
a=0
b=0
c=0
i=0
##### GPIO  #######
GPIO,setmode(GPIO.BOARD)
GPIO.cleanup()
readout1=38
readout2=37
readout3=36
heating1=01
heating2=02
heating3=04
ground1=06
ground2=25
ground3=14
### setting up the pins
r1=GPIO.setup(readout1, GPIO.IN)
h1=GPIO.setup(heating1, GPIO.OUT)
r2=GPIO.setup(readout2, GPIO.IN)
h2=GPIO.setup(heating2, GPIO.OUT)
h3=GPIO.setup(readout3, GPIO.IN)
h4=GPIO.setup(heating3, GPIO.OUT)

#### main program #####
while(i== 1 and n==exit):

   user_data_low = input('prompt the users to enter a two digit number ')
   user_data_high = input('prompt the users to enter a two digit number ')
   f.write(user_data_low)
   f.write(user_data_high)
   while (i <= 100000 or n== reset):
      if (i<= 100000):
          n = input('if you made a mistake when input your intial values type reset.')
      if (i !=1 and n==reset):
         i=i+1
         if(i == 1 or n==reset):
            print(int_nom+ratio() +"and"+ pt_for_inr())
            if(n==input('just type reset')):
                n = input('type exit if you have or accidental wanted to restart to quit other wise it not going to prefrom a last check')
   if (n!=1 or n < 1 and  n==exit):
      print(int_nom_rat()+  " and "+  pt_())
   
### i got to figure out how to make INR calculation
class int_nom_rat:
   def int_nom_ratio(self):
     inr = (pt/ptnom)^isitest
	 if (inr < user_data_low):
		return (inr + "your level are to low")
	 elif (user_data_low <= inr and inr <= user_data_high):
	    return(inr + your levels are right on)
	 else:
		return(inr + your level are to high)

#### isi 

isitest = isiref*slope


### create the logirithm slope of a b and c

### slope
class detla:
   def ___A__B___C(self):
     if(a < b ):
        return
     else:
         slope = (a-c)/(b-c)

###last one #####
class final:
   def searching__the_last(self):
     if (size == 0):
        return
     else:
        f.readline(size-1)
		f.close()
class pt__for_inr:
   def pt_(self):
	  f1 = open(datapoints)
	  pt1 = input(pt1)
	  pt2 = input(pt2)
	  pt3 = input(pt3)
	  pt4 = input(pt4)
	  pt5 = input(pt5)
	  pt6 = input(pt6)
	  d = timedelta(microseconds=-1)
	  (d.seconds, d.mircosends)
	  t1= (20,0)
	  pt=(r1/t1) 

#### writing it to a file then adding it to that and printing it out
