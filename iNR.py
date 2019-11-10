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
#from datetime import timedelta
#from threading


#### variables ####
#ptdrawc2= input('INR')
#ptnomdrawc2= int(ptdrawc2)
##### GPIO  #######

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



class LightSensor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection= reflection
    
    def reset():
       GPIO.cleanup()
       print("Gpio Cleanup has been done")
    
    
    def light_Sensor(self):
        delta_time = 0.0
        value= True
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
        '''
        This  that the time should be below 90.0 second or until the value read true  
        '''
        while ( (time.perf_counter - init_time) < 90.0   or  value == True):
            refc= GPIO.input(self.reflection)
            led_on
            time.sleep(.0000000001)
            final_time = time.perf_counter()
            if refc == 0:
               led_on
               time.sleep(.0000000001)
               delta_time=final_time-init_time
            elif .01<= refc and refc <= .99:
               led_on
               time.sleep(.0000000001)
               delta_time=final_time -init_time
            else: 
               GPIO.output(self.light,GPIO.LOW)
               delta_time = final_time - init_time
               value = False
        return delta_time
#### this is the class that will be defined as how the device will calculate the ptt\ptNorm  values
class ptt_and_norm_reader(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection = reflection
    def ptt_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print(" PTT LightSenors array in use")
        light_sensor=l_sensor.light_Sensor()
        l_sensor.reset()
        return light_sensor
    def norm_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print("Norm LightSenors array in use")
        light_sensor=l_sensor.light_Sensor()
        l_sensor,reset()
        return light_sensor
    def ptt_reader(self):
        pt_drawing = self.ptt_draw()
        return pt_drawing
    def norm_reader(self):
        norm_drawing = self.norm_draw()
        return norm_drawing


'''
these are the four threads that I am trying to run to get any average for the individual 
'''
       
def main(): 
   ''' 
   each sensor is being called
   '''
   l_sensor0 = LightSensor(24,18)
   l_sersor1 = LightSensor(23,17)
  # l_sensor2 = LightSensor(22,16)
  # l_sensor3 = LightSensor(25,12)
   '''
   each value of the sensor is being retuend then printed
   '''
   val_sensor0 = l_sensor0.light_Sensor()
   val_sensor1 = l_sensor1.light_Sensor()
   #val_sensor2 = l_sensor2.light_Sensor()
   #val_sensor3 = l_sensor3.light_Sensor()
   '''
   what each value is being sent to the manchine
   '''
   print(val_sensor0)
   print(val_sensor1)
   #print(val_sensor2)
   #print(val_sensor3)
   
   l_senor0.reset()

if __name__ == "___main___":
    main()
''' this is any artifact in which I need to find out how it workes
GPIO.add_event_callback(l_Sensor0 , t1)
GPIO.add_event_callback(l_Sensor1 , t2)
GPIO.add_event_callback(l_Sensor2 , t3)
GPIO.add_event_callback(l_Sensor3 , t4)
'''


