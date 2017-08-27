#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### dependencies ##### 
import math
import time
import numpy as np 
import sys
import RPi.GPIO as GPIO, time, os
import threading 
import collections
from datetime import timedelta
#### variables ####
inr = 0.0
value=0
counter=1
counters=0
i=0
d = timedelta(microseconds=-1)
(d.seconds, d.mircoseconds)
time=(50,0)
prothrombinTime = 0.0
ProthrombinNormal = 0.0
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
bar = "Fu"
result={}
slope_dict={}
pnom_dict={}
isi_dict={}
pt_dict={}
ptdrawc1= r1/t1+r2/t1/2#  mm/ seconds 
ptdrawc2= input('pt')
ptnomdrawc1= r3/t1+r4/t1/2
ptnomdrawc2= input('pt normal')
innervalue = 0
##### GPIO  #######
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
readout1=38
readout2=37
readout3=36
readout4=40
powerlight1=1
powerlight2=17
l1ght1=2
light2=4
ground1=6
ground2=14
button1=16
button2=18
button3=15
### setting up the pins
r1=   GPIO.setup(readout1, GPIO.IN)
h1=   GPIO.setup(light1, GPIO.OUT)
r2=   GPIO.setup(readout2, GPIO.IN)
h2=   GPIO.setup(heating2, GPIO.OUT)
r3=   GPIO.setup(readout3, GPIO.IN)
r4=   GPIO.setup(reading4, GPIO.IN)
rp1=  GPIO.setup(powerlight1, GPIO.OUT)
rp2=  GPIO.setup(powerlifhr2, GPIO.OUT)
but1= GPIO.setup(button1, GPIO.IN)
but3= GPIO.setup(button3,GPIO.IN)
but2= GPIO.setup(button2, GPIO.IN)
#### main program #####
### me implementing a merge sort for after
def msort(x):
 results=[]
 if len(x < 2):
  return x
 mid = int(len(x)/2)
 y= msort (x[:mid])
 z= msort (x[mid:])
 i = 0
 j = 0
 while i <len(y) and j <len(z):
  if y [i] > z[j]:
   result.append(z[j])
   j += 1
  else:
   result.append(y[i])
   i +=1
 result += y[i:]
 result += z[j:]
 return results
class lightsenors:
    def reflection():
        if (true):
            return "possible clotting"
        else:
            return false

    def lightsenor1(r1,rp1,t1):
        count = 0
        while (true or count == t1):
            GPIO.start.r1()
            GPIO.start.rp1()
            if ( GPIO.start.r1() != relfection()):
                for count in t1:
                  light = count.r1().reflection() # this is going to count how long it takes to create a relfection
              else:
                  GPIO.stop.r1()
                  GPIO.stop.rp1()
                  break


                
#### this is the class that will be defined as the intial pt values
class pt_for_inr:
   def ptDraw1(r1,l1):
       for count in (t1):
           

 def close_pt(ptdrawc1,ptdrawc2):
  lg1=ptdrawc1[0]
  la1=ptdrawc1[1]
  lg2=ptdrawc2[0]
  la2=ptdrawc2[1]
  innervalues = ((lg1 - la1)**2 + (lg2-la2)**2)
  return math.sqrt(innervalues)
 # set pt_ to a new method by using the distance formula
 def pt__(self, ptdrawc1, ptdrawc2):
 # for counter in range(counter,31):
   self.ptdelta= ptdrawc1-ptdrawc2
   return self.ptdelta
# set a point at which to appended the values 
 def appendingpt(self, ptdelta, ptdrawc1,ptrdrawc2):
  self.ptdelta.append(ptdelta)
  self.ptdrawc1.append(ptdrawc1)
  self.ptdrawc1.append(ptdrawc2)
 #this is going to be the try value that we are going to using to define  how closeness of the proximotiy to the patents own blood.
  def patents__pt( self,r1,r2,t1):
   if (patents_pt > close_pt(patents_pt,slope__isi)):
     self.pt=((r1/t1)+(r2/t1))/2
     ptcomp=map(lambda x,y:x-y,self.pt,self.ptdelta)   
   else:
    for l in range(l,1):
      return self.pt	 
      l += 1
  else:
      return None
# this is used to create a class for the ptnom in the inr to use 
class ptnom__for__inr:
 def close__ptnom(ptnomdrawc1 , ptnomdrawc2):
  lg1=ptnomdrawc1[0]
  la1=ptnomdrawc1[1]
  lg2=ptnomdrawc2[0]
  la2=ptnomdrawc2[1]
  #why was i setting this up?
  #Maybe for correctional regions 
  innervalues = ((lg1-la1)**2 + (lg2-lg2)**2)
  #where are these vaule begin used 
  return math.sprt(innervalue) 
 def appending__pt__noms(self, ptnomdrawc1,ptnomdrawc2):
  self.ptnomdelta = ptnomdrawc1 - ptnomdrawc2
  return self.ptnomdelta
 def patent_pt__noms(self):
  if (patent_pt_noms > close_ptnom(patent_pt_noms,slope_isi)):
   self.ptnom= (r3/t1)+(r4/t1)/2
   ptcom = map(lambda x,y: x-y, self.ptnom,self.ptnomdelta)
   for k in range(k,1):
    self.ptnom= (r3/t1)+(r4/t1)/2
    k += 1
    return ptnom
  else:
      return None

  
   
      
class detla:
 def slope__isi(self):
  if(a < b ):
   return 0
  else:
   return math.log(patent_pt())-math.log(ptnormallows())/math.log(close_pt())-math.log(ptnormallow())
class main_expression:
 def main():
  while(i== 1 and n==exit):
   user_data_low = input('prompt the users to enter a two digit number ')
   user_data_high = input('prompt the users to enter a two digit number ')
   print(int_nom_ratio +  " and "+ patents_pt)
   return result[]
   
### i got to figure out how to make INR calculation
class int_nom_rat:
 def int_nom_ratio(self):
  self.inr = (patents_pt()/ptnom())^isitest()
  if (inr < user_data_low):
   return (inr + "your level is too low")
  elif (user_data_low <= inr and inr <= user_data_high):
   return(inr + 'your levels are right on')
  else:
   return(inr + 'your level is too high')

#### isi 
#this is going to be a hard set to .7 or 1.4
isitest = isiref*slope
##isiref is based upon the reagents that are used to compare them 
  

###last one #####
class final:
   def searching__the_last(self):
     if (size == 0):
		return None
     else:
		return  result[i-1]
