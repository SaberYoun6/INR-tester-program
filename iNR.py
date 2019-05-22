#!/usr/bin/env python3
#author: Samuel Young
#
#
#
###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

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
    def reflections(self):
        if self:
            return True
        else:
            return False
    def light_Senor(self):
        count = 0
        value= False
        print("setup pins the And checking system to verify that it works")
        GPIO.setup(self.reflection, GPIO.OUT)
        GPIO.output(self.reflection,GPIO.LOW)
        GPIO.setup(self.light,GPIO.OUT) 
        GPIO.output(self.light,GPIO.HIGH)
        time.sleep(15.0)

        print("Setup the input pin")
        GPIO.setup(self.reflection,GPIO.IN)
        print( "Firing up the collection tools")
        print(type(count))
        print(type(value))
        init_time= time.perf_counter()
        while (1 or (!value)):
            print("pin input authorized")
            refc= GPIO.input(self.reflection)
            if refc == 0:
               print("LED on")
               GPIO.output(self.light,GPIO.HIGH)
               count =+ 1 
               if count == 50:
                   value =True
            elif .01<= refc and refc <= .99:
               
               GPIO.output(self.light,GPIO.HIGH)
            else: 
               GPIO.output(self.light,GPIO.LOW)
               value = True
            '''if ( value == refc.reflection()):
                print(count)
            else:
                print("Light should be turning off")
                light_n = GPIO.output(self.light,GPIO.LOW)
                print(count)
                '''
        return count
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
        return pt_drawing

      
      
def main():
    l_senor=LightSenor(24,18) 
    value=l_senor.light_Senor()
    print(value)
    #ptt_reader0=ptt_and_norm_reader(24,18) #(light,senor)  ,ptt_reader1=,ptt_and_norm_reader(8,40)
    #result0 = ptt_reader0.ptt_and_norm()#,result1= ,ptt_reader2.ptt_and_norm()
    #print(result0)
main()

