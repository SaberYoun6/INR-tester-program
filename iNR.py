#!/bin/bash/python
#author: Samuel Young
#
#
#
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
bar = "Fu"
thresold=4.5
result={}
slope_dict={}
pnom_dict={}
isi_dict={}
pt_dict={}
ptdrawc2= input('INR')
ptnomdrawc2= int(ptdrawc2)
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
GPIO.setup(readout1, GPIO.IN)
GPIO.setup(light1,   GPIO.OUT)
GPIO.setup(readout2, GPIO.IN)
GPIO.setup(heating2, GPIO.OUT)
GPIO.setup(readout3, GPIO.IN)
GPIO.setup(reading4, GPIO.IN)
GPIO.setup(powerlight1, GPIO.OUT)
GPIO.setup(powerlight2, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setWarings(False)
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
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i+=1
            result += y[i:]
            result += z[j:]
            return result
def distance(self,a):
    inval=((self-a)**2 + (self-a)**2)
    dist=math.sqrt(inval)
    return dist
class lightsenors:
    def reset():
       return None
    def change(self,a,threshold):
       if ( reset() != self.weight(a) or null = self.weight(a) ):
           return None
       elif (self.weight(a)=> threshold ):
          x = self.weight(a)+1
       return x
    def reflection():
        if (True):
            return True 
        else:
            return False
    def weight(self,a,threshold):
       if( a <= self.change(a,threshold)):
           return None
       else:
            x = a + self.weight(a)
       return x
# r stands for reading in , rp  stands for readingout point, t stand for time, and s is for weight of  slip
    def lightsenor(self,r,rp,t,s):
        count = 0
        while (True or count <= t):
            GPIO.start.r()
            GPIO.start.rp()
            if ( GPIO.start.r() != relfection()):
                if (GPIO.start.r() != weight(s)):
                    GPIO.stop.r()
                    GPIO.stop.rp()
                else:
                    for count in t:
                          light = r().reflection() / count # this is going to count how long it takes to create a relfection
                          return light
            else:
                GPIO.stop.r()
                GPIO.stop.rp()
                break
#### this is the class that will be defined as the intial pt values
class pt_for_inr:
    def ptDraw(readout1,light1,t1,readout2,slip):
        if (lightsenors.weight(slip,theshold) >= threshold):
             lightSenor1 = lightsenors.lightsenor(readout1,light1,t1)
             lightSenor2 = lightsenors.lightsenor(readout2,light1,t1)
             if (lightSenor1 <= lightSenor2):
                uplimit  = lightSenor1.distance(lightSenor2) 
                x= uplimit
             elif (lightSenor1 == lightSenor2):
                x= lightSenor1
             else:
                lowerlimit= lightSenor2.distance(lightSenor1)
                x= lowerlimit
        else:
            return None
        return x


#def ptdelta():
 #set pt_ to a new method by using the distance formula
#def pt__( uplimit, lowerlimit):
# for counter in range(counter,31):
#  if (uplimit):
#  self.ptdelta= ptdrawc1-ptdrawc2
def appendingpt(self, ptdelta, ptdrawc1,ptrdrawc2):
self.ptdelta.append(ptdelta)
self.ptdrawc1.append(ptdrawc1)
# self.ptdrawc1.append(ptdrawc2)
#this is going to be the try value that we are going to using to define  how closeness of the proximotiy to the patents own blood.
    def patents__pt( self,r1,r2,t1):
    if (pt_for_inr.patents_pt > .ptnom__for_inr.close_pt(patents_pt,slope__isi)):
         self.pt=pt_for_inr.ptdraw(r1,rp1,t1,r2,)/2
         ptcomp=map(lambda x,y:x-y,self.pt,self.ptdelta)   
       else:
        for l in range(l,1):
          return self.pt	 
          l += 1
      else:
          return None
# this varialbe in which is called close pt will find out how close the approximate to each the dataset that was set forth 
      def close_pt():
      delta 




# this is used to create a class for the ptnom in the inr to use 
class ptnom__for__inr:
    def ptnomdraw(readout3,light2,readout4,t2,slip):
## slide = standard weight of the slides ,t2 is a timer that i similarly set as timer one , this will be an input into the system, light2 will flash continuiosly until it hit the reflection point, readout 4 is another input variable that should readout similarly to the readout 3
    lightsenor3 = lightsenors.lightssenor(readout3,light2,t2)
    lightsenor4 = lightsenors.lightssenor(readout4,light2,t2)
     

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
            ptnom= pt_for_inr.ptdraw1(r1,rp1,t1,r2,rp2)
            ptcom = map(lambda x,y: x-y, self.ptnom,self.ptnomdelta)
            for k in range(k,1):
                self.ptnom= (r3/t1)+(r4/t1)/2
                k += 1
                return ptnom
        else:
        return None

  
   
      
class detla:
    def slope__isi(self,a):
        if(self < a ):
            return None
        else:
            return math.log(patent_pt())-math.log(ptnormallows())/math.log(close_pt())-math.log(ptnormallow())
class main_expression:
    def main():
        while(i== 1 and n==exit):
            user_data_low = input('prompt the users to enter a two digit number ')
            user_data_high = input('prompt the users to enter a two digit number ')
            print(int_nom_rat.int_nom_ratio() +  " and "+ patents_pt)
            return result[]
   
### i got to figure out how to make INR calculation
class int_nom_rat:
    def int_nom_ratio(self):
        self.inr = (inr_.patents_pt()/ptnom())^isitest()
        if (inr < user_data_low):
            inrstatus= (inr + "your level is too low")
        elif (user_data_low <= inr and inr <= user_data_high):
            inrstatus= (inr + 'your levels are right on')
        else:
            inrstatus=(inr + 'your level is too high')
        
        return inrstatus

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

##
main_expression.main()

