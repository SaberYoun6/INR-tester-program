#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### variables ##### 
import math
import time
import numpy as np s
import sys
import RPi.GPIO as GPIO
import threading 
import collections
from dateime import timedelta

f=open('~/Documents/bloodtest','r+a')
inr = 0.0
header=(size-2)
value=0
counter=1
counters=0
i=0
f1 = open('~/Documents/datapoints','w')
f2 = open('~/Documents/datapoints','r')
d = timedelta(microseconds=-1)
(d.seconds, d.mircoseconds)
t1=(20,0)
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
pt_dict={}
ptdrawc1= r1/t1+r2/t1/2#  mm/ seconds 
ptdrawc2= input('pt')
ptnomdrawc1= r3/t1+r4/t1/2
ptnomdrawc2= input('pt normal') 
##### GPIO  #######
GPIO,setmode(GPIO.BOARD)
GPIO.cleanup()
readout1=38
readout2=37
readout3=36
readout4=40
heating1=1
heating2=2
heating3=4
headtin4=17
ground1=6
ground2=25
ground3=14
button1=16
button2=18
### setting up the pins
r1=GPIO.setup(readout1, GPIO.IN)
h1=GPIO.setup(heating1, GPIO.OUT)
r2=GPIO.setup(readout2, GPIO.IN)
h2=GPIO.setup(heating2, GPIO.OUT)
r3=GPIO.setup(readout3, GPIO.IN)
h3=GPIO.setup(heating3, GPIO.OUT)
r4=GPIO.setup(reading4, GPIO.IN)
h4=GPIO.setup(heating4, GPIO.OUT)
but1=GPIO.setup(button1, GPIO.IN)
but2=GPIO.setup(button2, GPIO.IN)
#### main program #####
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
   result.appnd(y[i])
   i +=1
 result += y[i:]
 result += z[j:]
 return results
class pt__for_inr:
 def close_pt(ptdrawc1,ptdrawc2):
  lg1=ptdrawc1[0]
  la1=ptdrawc1[1]
  lg2=ptdrawc2[0]
  la2=ptdrawc2[1]
  innervalue = 0
  innervalues += ((lg1 - la1)**2 + (lg2-la2)**2)
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
 #this is going to be the try value that we are going to using to define  how closenss of the proximotiy to the patents own blood.
  def patents__pt(self):
   if (patents_pt in close_pt(patents_pt,slope__isi)):
     self.pt=((r1/t1)+(r2/t1))/2
     ptcomp=map(lambda x,y:x-y,self.pt,self.ptdelta)   
   else:
    for l in range(l,1):
      return self.pt	 
      l += 1
# this is used to create a class for the ptnom in the inr to usd
class ptnom__for__inr:
 def close__ptnom(ptnomdrawc1 , ptnomdrawc2):
  lg1=ptnomdrawc1[0]
  la1=ptnomdrawc1[1]
  lg2=ptnomdrawc2[0]
  la2=ptnomdrawc2[1]
  innervalues= 0
  innervalues += ((lg1-la1)**2 + (lg2-lg2)**2)
  return math.sprt(innervalue) 
 def appending__pt__noms(self, ptnomdrawc1,ptnomdrawc2):
  self.ptnomdelta = ptnomdrawc1 - ptnomdrawc2
  return self.ptnomdelta
 def patent_pt__noms(self):
  if (patent_pt_noms in close_ptnom(patent_pt_noms,slope_isi)):
   self.ptnom= (r3/t1)+(r4/t1)/2
   ptcom = map(lambda x,y: x-y, self.ptnom,self.ptnomdelta)
   for k in range(k,1):
    self.ptnom= (r3/t1)+(r4/t1)/2
    k += 1
    return ptnom
  
   
      
class detla:
 def slope__isi(self):
  if(a < b ):
   return 0
  else:
   return math.log(patent_pt)-math.log(ptnormallows)/math.log(close_pt)-math.log(ptnormallow)
class main_expression:
 def main():
  while(i== 1 and n==exit):
   user_data_low = input('prompt the users to enter a two digit number ')
   user_data_high = input('prompt the users to enter a two digit number ')
   print(int_nom_ratio +  " and "+ patents_pt)
   
### i got to figure out how to make INR calculation
class int_nom_rat:
 def int_nom_ratio(self):
  self.inr = (patents_pt/ptnom)^isitest
  if (inr < user_data_low):
   return (inr + "your level are to low")
  elif (user_data_low <= inr and inr <= user_data_high):
   return(inr + 'your levels are right on')
  else:
   return(inr + 'your level are to high')

#### isi 
#this is going to be a hard set to .7 or 1.4
isitest = isiref*slope
##isiref is based upon the reagents that are used to compare them 
  

###last one #####
class final:
   def searching__the_last(self):
     if (size == 0):
        return
     else:
         f.readline(size-1)
#### writing it to a file the` adding it to that and printing it out
f.close()
f1.close()
f2.close()
