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
class LightSenors(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection= reflection
    def reset(self):
       GPIO.cleanup()
       print("Gpio Cleanup has been done")
    def reflection(self):
        if self:
            return True
        else:
            return False
    def lightSenor(self):
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
        while (value == True ):
            refc= GPIO.input(self.reflection)
            light_p =GPIO.output(self.light,GPIO.HIGH)
            if ( not refc.relfection()):
                count = time.perf_counter()
                print(count)
            else:
                print("Light should be turning off")
                light_n = GPIO.output(self.light,GPIO.LOW)
                print(count)
                value= True
        return count
#### this is the class that will be definedas how the device will calculate the ptt\ptNorm  values
class ptt_and_norm_reader:
    def __init__(self,light, reflection):
        self.light = light
        self.reflection = reflection
    def ptt_and_norm_draw(self):
        l_senor=LightSenors(self.light,self.reflection)
        print(" PTT\PTNorm LightSenors array in use")
        light_senor=l_senor.lightSenor()
        l_senor.reset()
        return light_senor
    def ptt_and_norm(self):
        pt_drawing = self.ptt_and_norm_draw()
        return pt_drawing

      
      
def main():
    ptt_reader0=ptt_and_norm_reader(38,24)# ,ptt_reader1=,ptt_and_norm_reader(8,40)
    result0 = ptt_reader0.ptt_and_norm()#,result1= ,ptt_reader2.ptt_and_norm()
    print(result0)
main()

