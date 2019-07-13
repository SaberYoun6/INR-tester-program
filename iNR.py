#!/usr/bin/env python3
#author: Samuel Young
#
#
#
###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

# 
# 
#
__author__ = "Samuel Young"
__copyright__ =" Copyright 2016, The INR project"
__credits__ = ["Samuel Young"]
__license__ = "GPL"
__versoion__ = "0.0.5"
__maintianer__= "Samuel Young"
__email__ = "samuel.young.103@gmail.com"
__status__ = "pre-beta"
#### dependencies ##### 
import time
import RPi.GPIO as GPIO
import collections
from datetime import timedelta
#### variables ####
inr = 0.0
value=0
counters=0
i=0
#ptdrawc2= input('INR')
#ptnomdrawc2= int(ptdrawc2)
##### GPIO  #######
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
class LightSenor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection= reflection
    def reset(self):
       GPIO.cleanup()
       print("Gpio Cleanup has been done")
    def light_Senor(self):
        count = 0
        delta_time = 0.0
        value= False
        print("setting up  pins")
        GPIO.setup(self.reflection, GPIO.OUT)
        GPIO.output(self.reflection,GPIO.LOW)
        GPIO.setup(self.light,GPIO.OUT) 
        GPIO.output(self.light,GPIO.HIGH)
        time.sleep(7.5)
        print("Setup the input pin")
        GPIO.setup(self.reflection,GPIO.IN)
        print( "Firing up the collection tools")
        init_time= time.perf_counter()
        timer1=time.time()
        while ( 1  or  value == True):
            print("pin input authorized")
            refc= GPIO.input(self.reflection)
            GPIO.output(self.light,GPIO.HIGH)
            final_time = time.perf_counter()
            timer2=time.time()
            count = count + 1
            print (count)
            print(value)
            print(refc)
            if refc == 0:
               print("LED on")
               GPIO.output(self.light,GPIO.HIGH)
               print('Checking status of count : %d\n checking the inital time : %f\n' %(count, init_time) ) 
               timer2=time.time()
               if count == 359901:
                   value = True
                   print("exceed time granted")
                   delta_time = final_time - init_time
                   GPIO.output(self.light,GPIO.LOW)
                   final_timer = timer2-timer1
                   print(final_timer)
                   break
            elif .01<= refc and refc <= .99:
               print("LED on")
               GPIO.output(self.light,GPIO.HIGH)
               if count == 359901:
                   value = True
                   print("exceed time granted")
                   delta_time = final_time - init_time
                   GPIO.output(self.light,GPIO.LOW)
                   break
            else: 
               print("LED OFF")
               GPIO.output(self.light,GPIO.LOW)
               value = True
               delta_time = final_time - init_time
        return delta_time
#### this is the class that will be definedas how the device will calculate the ptt\ptNorm  values
class ptt_and_norm_reader:
    def __init__(self,light, reflection):
        self.light = light
        self.reflection = reflection
    def ptt_and_norm_draw(self):
        l_senor=LightSenor(self.light,self.reflection)
        print(" PTT\PTNorm LightSenors array in use")
        light_senor=l_senor.light_Senor()
        l_senor.reset()
        return light_senor
    def ptt_and_norm(self):
        pt_drawing = self.ptt_and_norm_draw()
        for i in pt_drawing:
           
        return pt_drawing

      
      
def main():
    l_senor=LightSenor(24,18) 
    value=l_senor.light_Senor()
    l_senor.reset()
    print(value)
    #ptt_reader0=ptt_and_norm_reader(24,18) #(light,senor)  ,ptt_reader1=,ptt_and_norm_reader(8,40)
    #result0 = ptt_reader0.ptt_and_norm()#,result1= ,ptt_reader2.ptt_and_norm()
    #print(result0)
main()

