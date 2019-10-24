#!/usr/bin/env python3
#
#
#
### Create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood. This is going to be used for to get the inital results for the INR ratio. then It'll be called again to figure out what is going on.  
# 
# 
#
__author__ = "Samuel Young"
__copyright__ =" Copyright 2016, The INR project"
__credits__ = ["Samuel Young"]
__license__ = "GPL"
__version__ = "0.0.7"
__maintianer__= "Samuel Young"
__email__ = "samuel.young.103@gmail.com"
__status__ = "beta"
#### dependencies ##### 

import time
import RPi.GPIO as GPIO
import collections
from datetime import timedelta
from threading import Thread, Lock


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



class LightSensor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection= reflection
    def reset(self):
       GPIO.cleanup()
       print("Gpio Cleanup has been done")
    def light_Sensor(self):
        count = 0
        delta_time = 0.0
        value= False
        print("setting up  pins")
        GPIO.setup(self.reflection, GPIO.OUT)
        GPIO.output(self.reflection,GPIO.LOW)
        GPIO.setup(self.light,GPIO.OUT) 
        #led_off= GPIO.output(self.light,GPIO.LOW)
        #time.sleep(7.5)
        print("testing light")
        led_on=GPIO.output(self.light,GPIO.HIGH)
        time.sleep(1)
        print("Setup the input pin")
        GPIO.setup(self.reflection,GPIO.IN)
        init_time= time.perf_counter()
        timer1=time.time()
        while ( 1  or  value == True):
            refc= GPIO.input(self.reflection)
            led_on
            time.sleep(.0000001)
            final_time = time.perf_counter()
            timer2 = time.time()
            count = count + 1
            if refc == 0:
               led_on
               timer2=time.time()
               if count == 359901:
                   value = True
                   delta_time = final_time - init_time
                   GPIO.output(self.light,GPIO.LOW)
                   break
            elif .01<= refc and refc <= .99:
               led_on
               time.sleep(.000001)
               if count == 359901:
                   value = True
                   delta_time = final_time - init_time
                   GPIO.output(self.light,GPIO.LOW)
                   break
            else: 
               GPIO.output(self.light,GPIO.LOW)
               value = True
               delta_time = final_time - init_time
               break
        return delta_time
#### this is the class that will be definedas how the device will calculate the ptt\ptNorm  values
class ptt_and_norm_reader:
    def __init__(self,light, reflection):
        self.light = light
        self.reflection = reflection
    def ptt_and_norm_draw(self):
        l_senor=LightSenor(self.light,self.reflection)
        print(" PTT\PTNorm LightSenors array in use")
        light_senor=l_sensor.light_Sensor()
        l_senor.reset()
        return light_senor
    def ptt_and_norm(self):
        pt_drawing = self.ptt_and_norm_draw()
        for i in pt_drawing:         
          return pt_drawing

def LightSensor_thread(*args):
       t = Thread(target =light_Sensor(), args=args)
       t.start()


main()
   
GPIO.add_event_callback((l_sensor0) , LightSensor_thread())
GPIO.add_event_callback((l_sensor1) , LightSensor_thread())
GPIO.add_event_callback((l_sensor2) , LightSensor_thread())
GPIO.add_event_callback((l_sensor3) , LightSensor_thread())

l_sensor0.reset()
l_sensor1.reset()
l_sensor2.reset()
l_sensor3.reset()

def main():      
   l_sensor0  =  LightSensor(24,18)
   l_sensor1  =  LightSensor(25,17)
   l_sensor2  =  LightSensor(24,16)
   l_sensor3  =  LightSensor(27,22)
   val_sensor0 = l_sensor0.light_Sensor()
   val_sensor1 = l_sensor1.light_Sensor()
   val_sensor2 = l_sensor2.light_Sensor()
   val_sensor3 = l_sensor3.light_Sensor()


    #ptt_reader0=ptt_and_norm_reader(24,18) #(light,senor)  ,ptt_reader1=,ptt_and_norm_reader(8,40)
    #result0 = ptt_reader0.ptt_and_norm()#,result1= ,ptt_reader2.ptt_and_norm()
    #print(result0)

# This should return the lightsensor arrays
