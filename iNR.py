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
         return(inr + 'your levels are right on')
      else:
          return(inr + 'your level are to high')

#### isi 

isitest = isiref*slope


### create the logirithm slope of a b and c

### slope
class detla:
   def ___A__B___C(self):
     if(a < b ):
        return
     else:
       slope= math.log(pnthigh)-math.log(pntlows)/math.log(pt)-math.log(pntlow)

###last one #####
class final:
   def searching__the_last(self):
     if (size == 0):
        return
     else:
         f.readline(size-1)
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
pt_dict={}
class pt__for_inr:
   def pt_(self, ptdelta):
      if (values>=1 or inputs==recalibartions):
         pnt1=(r1/t1)+(r2/t1)
         pnt1=pnt1/2
         pnt2=r1/t1+r2/t1
         pnt2= pnt2/2
         pnt3=r1/t1+r2/t1
         pnt3= pnt3/2
         pnt4=r1/t1+r2/t1
         pnt4= pnt4/2
         pnt5=r1/t1+r2/t1
         pnt5= pnt5/2
         pnt6=r1/t1+r2/t1
         pnt6= pnt6/2
         pnt7=r1/t1+r2/t1
         pnt7= pnt7/2
         pnt8=r1/t1+r2/t1
         pnt8= pnt8/2
         pnt9=r1/t1+r2/t1
         pnt9= pnt9/2
         pnt10=r1/t1+r2/t1
         pnt10= pnt10/2
         pnt11=r1/t1+r2/t1
         pnt11= pnt11/2
         pnt12=r1/t1+r2/t1
         pnt12= pnt12/2
         pnt13=r1/t1+r2/t1
         pnt13= pnt13/2
         pnt14=r1/t1+r2/t1
         pnt14= pnt14/2
         pnt15=r1/t1+r2/t1
         pnt15= pnt15/2
         pnt16=r1/t1+r2/t1
         pnt16= pnt16/2
         pnt17=r1/t1+r2/t1
         pnt17= pnt17/2
         pnt18=r1/t1+r2/t1
         pnt18= pnt18/2
         pnt19=r1/t1+r2/t1
         pnt19= pnt19/2
         pnt20=r1/t1+r2/t1
         pnt20= pnt20/2
         pnt21=r1/t1+r2/t1
         pnt21= pnt21/2
         pnt22=r1/t1+r2/t1
         pnt22= pnt22/2
         pnt23=r1/t1+r2/t1
         pnt23= pnt23/2
         pnt24=r1/t1+r2/t1
         pnt24= pnt24/2
         pnt25=r1/t1+r2/t1
         pnt25= pnt25/2
         pnt26=r1/t1+r2/t1
         pnt26= pnt26/2
         pnt27=r1/t1+r2/t1
         pnt27= pnt27/2
         pnt28=r1/t1+r2/t1
         pnt28= pnt28/2
         pnt29=r1/t1+r2/t1
         pnt29= pnt29/2
         pnt30=r1/t1+r2/t1
         pnt30= pnt30/2
	  
         for counter in range(counter,31):
            pt+counter = input(pt+counter)
            ptdelta+counter= pt+counter-pnt+counter
            for counters in range(counters,31): 
			    ptc+counters = 0 >= ptdelta+counters
                pt_dict = {[pnt+counter : ptc+counters ]}
                lambda(pnt+counters,ptdetla.counter,x-y)
	  else:
         for i in range(i,1):
            if(inputs== input(recalibrations) or values == 1):
               f2.read(size-1)
               pt = (r1/t1)+(r2/t1)/2
               f.write(pt)
               return pt	
            elif(inputs==input(recalibarations)):
               value = 0
               break
            else:
               f2.read(header)
               pt = (r1/t1)+(r2/t1)/2
               f.write(pt)
               return  pt


# this is used to create a class for the ptnom in the inr to usd
class ptnom__for__inr:
   def ptnom__(self):
      if (values >= 2 or inputs==recalibarations):
          ptnom1=r3/t1+r3/t1
          ptnom1=ptnom1/2
          ptnom2=r3/t1+r4/t1
          ptnom2=ptnom2/2
          ptnom3=r3/t1+r4/t1
          ptnom3=ptnom3/2
          ptnom4=r3/t1+r4/t1
          ptnom4=ptnom4/2
          ptnom5=r3/t1+r4/t1
          ptnom5=ptnom5/2
          ptnom6=r3/t1+r4/t1
          ptnom6=ptnom6/2
          ptno1= input(ptnom)
          ptno2= input(ptnom)
          ptno3= input(ptnom)
          ptno4= input(ptnom)
          ptno5= input(ptnom)
          ptno6= input(ptnom)
          ptnoc1= input(ptnom).compare(ptnom1)
          ptnoc2= input(ptnom).compare(ptnom2)
	      ptnoc3= input(ptnom).compare(ptnom3)
		  ptnoc4= input(ptnom).compare(ptnom4)
          ptnoc5= input(ptnom).compare(ptnom5)
          ptnoc6= input(ptnom).compare(ptnom6)
		  value`=value + 1
	      f1.write(ptnoc1+ ptnoc3 + ptnoc4 + ptnoc5 + ptnoc6)
	      for i in range(i,1):
			 if(inputs==input(recalibaration)):
                values=0
				break
			 else:
                f2.read(size-1)

				ptnom= (r3/t1)+(r4/t1)/2
                f.write(ptnom)
                return ptnom
#### writing it to a file the` adding it to that and printing it out
f.close()
f1.close()
f2.close()
