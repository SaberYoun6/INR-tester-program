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
counters=0
i=0
d = timedelta(microseconds=1)
#(d.seconds, d.mircoseconds)
prothrombinTime = 0.0
ProthrombinNormal = 0.0
isitest=0
slope=0
isiref=0
user_data_low = 0.0
user_data_high = 0.0
tester_data =0.0
weight_thesrold= 1 
bar = "Fu"
thresold=4.5
result={}
slope_dict={}
pnom_dict={}
isi_dict={}
pt_dict={}
#ptdrawc2= input('INR')
#ptnomdrawc2= int(ptdrawc2)
##### GPIO  #######
GPIO.setmode(GPIO.BOARD)
readout1=38
readout2=37
readout3=36
readout4=40
powerlight1=1
powerlight2=17
global l1ght1
global light2
ground1=6
ground2=14
buttonup=16
buttonselection=18
buttondown=15
weights=22
### setting up the pins
#GPIO.setup(weights,GPIO.IN)
#GPIO.setup(readout1, GPIO.IN)
#GPIO.setup(light1, GPIO.OUT)
#GPIO.setup(light2, GPIO.OUT)
#GPIO.setup(readout2, GPIO.IN)
#GPIO.setup(heating2, GPIO.OUT)
#GPIO.setup(readout3, GPIO.IN)
#GPIO.setup(readout4, GPIO.IN)
#GPIO.setup(powerlight1, GPIO.OUT)
#GPIO.setup(powerlight2, GPIO.OUT)
#GPIO.setup(buttonup, GPIO.IN)
#GPIO.setup(buttondown, GPIO.IN)
#GPIO.setup(buttonselection, GPIO.IN)
#GPIO.setWarnings(False)
#### main program #####
### me implementing a merge sort for after
#def msort(x):
#    results=[]
#    if len(x < 2):
#         return x
#    mid = int(len(x)/2)
#    y= msort (x[:mid])
#    z= msort (x[mid:])
#    i = 0
#    j = 0
#    while i <len(y) and j <len(z):
#        if y[i] > z[j]:
#            result.append(z[j])
#            j += 1
#        else:
#            result.append(y[i])
#            i+=1
#            result += y[i:]
#            result += z[j:]
#            return result
#def distance(self,a):
#    inval=((self-a)**2 + (self-a)**2)
#    dist=math.sqrt(inval)
#    return dist
class LightSenors(object):
    def reset(self):
       return None
    def change(self,a,weight_threshold):
       if ( self.reset() != self.weight(a) or self.weight(a) == None ):
           x = 0
       elif (self.weight(a,) >= weight_threshold ):
           x = self.weight(weights)+1
       else:
           x= None
       return x
    def reflection(self,rp):
        if (rp == True):
            return True 
        else:
            rp = False
        self.reflection(rp,rp)
    def weight(self,a,weight_threshold):
       if( a <= self.change(a,)):
           return None
       else:
            x = a + self.weight(a,)
       return x
# r stands for r  , rp  stands for readingout point, t stand for time, and s is for weight of  slip
    def lightSenor(self,rp,r,s):
        count = 0
        GPIO.setup(r,GPIO.IN)
        GPIO.setup(rp,GPIO.OUT)
        GPIO.setup(s,GPIO.IN)
        while (True or count <= t):
            refc=GPIO.input(r)
            refp=GPIO.output(rp,1)
            if ( GPIO.start.r() != LightSenors.relfection(rp)):
                if (GPIO.start.r() != weight(gpio.input(s),)):
                    refc.stop()
                    refp.stop()
                    GPIO.cleanup()
                else:
                    if refcx != refp:
                        count = time.perf_counter_ns()
                    else: 
                        lightCont = r().LightSenors.reflection(rp()) / count # this is going to count how long it takes to create a relfection
                        return lightCont
            else:
                refc.stop()
                refp.stop()
                GPIO.cleanup()
                continue 
#### this is the class that will be defined as the intial pt values
class ptReader:
    def ptDraw(self,r1,r2,l1,l2,s):
        lsenor=LightSenors()
        lightSenor1= lsenor.lightSenor(l1,r1,s)
        lightSenor2=lsenor().lightSenor(l2,r2,s)
        if (lightSenor1 <= lightSenor2):
            uplimit  = lightSenor1.distance(lightSenor2) 
            ptt= uplimit
        elif (lightSenor1 == lightSenor2):
            ptt= lightSenor1
        else:
            lowerlimit= lightSenor2.distance(lightSenor1)
            ptt= lowerlimit
        LightSenors.reset()
        return ptt
    def ptstats(self):
        light1=2
        light2=4
        while True:
            return self.ptDraw(readout1,readout2,light1,light2,weights)
      
### this is the class in which is used to define two other senours and wihat they are used for

class ptNormReader():
    def ptNormDraw(self,readout3,readout4,light1 ,light2,weights,threshold):
        lightSenors3,lightSenors4=LightSenors.lightSenors(readout3,light1,weights),LightSenors.lightSenors(readout4,light2,weights)
        if (lightSenors3<= lightSenors4):
            uplimit= lightSenors3.distnace(lightSenors4)
            ptnorm = uplimit
        elif (lighSenors3 == lightSenors4):
            ptnorm =lightSenors4
        else:
            lowerlimt= lightSenors4.distance(lightSenors3)
            ptnorm =lowerlimit
        LightSenors.Reset()
        return ptnorm


#class mainExpression:
def main():
    rList=[2,5,7,9,10,11]
    if ptReader().ptstats() == False:
         print(ptReader().ptstats())
    else :
         print(bytes(rlist))

           
#mainExpression.main()
main()
