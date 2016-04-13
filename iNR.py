#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### variables ##### 
import numpy
import math
import time
import numpy as np
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
ptdraw= r1/t1+r2/t1/2#  mm/ seconds 
ptdrawc= input('pt')
ptnomdraw= r3/t1+r4/t1/2
ptnomdraw= 
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
def msort(x)
 results=[]
 if len(x < 2:
  return x 
 mid = int(len(x)/2)
 y=msort(x[:mid])
 z= msort(x:mid:])
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
   def pt_(ptdraw,ptdrawc):
      lg1=ptdraw[0]
      la1=ptdraw[1]
      lg2=ptdrawc[0]
      la2=ptdrawc[1]
      return closePT = arccos(sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lg1-lg2)
   def pt__(self)
    for counter in range(counter,31):
      'ptdelta'+counter= ptdraw-ptdrawc
      if('ptc'+counter = 0 or 0 >= 'ptdelta'+counter and 'ptdelta'+counter <= 0):
         'ptc'+counter = 'ptc'+counter - ptdelta
              else:
				   ptc+counter == ptdetla+counter
				   continue
                   pt_dict = {['pnt'+counters], ['ptc'+counters]}
                   ptcomp=map(lambda x,y:x-y,'pnt'+counters,'ptdelta'+counters)
				   pt=((r1/t1)+(r2/t1))/2
				    
	               else:
                      for i in range(i,1):
    		             if(inputs== input(recalibrations) or values == 1):
                             f2.read(size-1)
                             f.write(pt)
                             return pt	
                             elif(inputs==input(recalibarations)):
                             value = 0
                             break
                             else:
                             ptjoint2=f2.read(header)
                             f.write(pt)
# this is used to create a class for the ptnom in the inr to usd
class ptnom__for__inr:
 def ptnom__(ptnomdraw , ptnomdrawc):
      lg1=ptnomdraw[0]
      la1=ptnomdraw[1]
      lg2=ptnomdrawc[0]
      la2=ptnomdrawc[1]
      return closestpt= arccos(sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lg1-lg2)
 def ptnoms(self)
  if (values >= 2 and values!=1 or inputs==recalibarations):
   for counter in range (counter, 37) 
    'ptnom'+counter=r3/t1+r4/t1
    'ptnom'+counter='ptnom'+counter/2
    'ptno'+counter= input(ptnom)
    'ptnomdelta'+counter= 'ptnom'+counter-'ptno'+counter
    'ptnoc'+counter = 'ptnom'+counter-'ptnomdelta'+counter;
    'ptnoTF'+counter=ptnoc
    value=value + 1
    f1.write(ptnoc1+ ptnoc3 + ptnoc4 + ptnoc5 + ptnoc6)
    for i in range(i,1):
     ptnom= (r3/t1)+(r4/t1)/2
     f.write(ptnom)
     return ptnom
      if(inputs==input(recalibaration)):#i'm hoping that it will rest the values back to zero then it will change allow the change o the varable type
        values=0
        break
      else:
      f2.read(size-1)
     
class detla:
   def ___A__B___C(self):
     if(a < b ):
        return 0
     else:
       slope= math.log(pt)-math.log(ptnormallows)/math.log(highestpt)-math.log(ptnormallow)
class main_expression:
 def main()
  while(i== 1 and n==exit):

   user_data_low = input('prompt the users to enter a two digit number ')
      user_data_high = input('prompt the users to enter a two digit number ')
   f1.write(user_data_low)#these are to 
   f1.write(user_data_high)
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
         return(inr + 'your levels are right on')
      else:
          return(inr + 'your level are to high')

#### isi 
#this is going to be a hard set to .7 or 1.4
isitest = isiref*slope
##isiref is based upon the reagents that are used to compare them 

### create the logirithm slope of a b and c

### slope

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
