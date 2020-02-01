#!/usr/bin/env python3
#
#
#
### Create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood. This is going to be used for to get the inital results for the INR ratio. then It'll be called again to figure out what is going on.  
# 
# 
#
__author__ = "Samuel Young"
__copyright__ = " Copyright 2016, The INR project"
__credits__ = ["Samuel Young"]
__license__ = "GPL"
__version__ = "0.0.845"
__maintianer__ = "Samuel Young"
__email__ = "samuel.young.103@gmail.com"
__status__ = "beta"

#### dependencies #####
import time
from gpiozero import LED, LightSensor
import collections


# from datetime import timedelta
# from threading


class IrSensor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection = reflection

    @property
    def __iRDectector__(self):
        change_time = 0.0
        
        read_value = False

        print("setting up  pins")

        ir_light = LED(self.light)

        start_timer = time.perf_counter()
        '''
        This  that the time should be below 90.0 second or until the value does read as true  it must be reaching the value 
        '''
        while (time.perf_counter() - start_timer) <= 90.0 or (read_value is True):
            finish_timer = time.perf_counter()
            print("Running with senors")
            #this is me setting up the ligth reflection with a certain threshold
            i_r_detection = LightSensor(self.reflection, threshold=.99)
            # this turn the light on for test reason
            ir_light.on()
            #this is a call to wait for light 
            # this should allow for a better print out
            # it threshold is less then the intital call then it wouldn't detect
            if i_r_detection.wait_for_dark() :
                change_time = finish_timer - start_timer
                read_value = False
            #if the threshold is greater then the value it will return with a value of the changes
            elif i_r_dectection.wait_for_light(.001):
                change_time = finish_timer - start_timer
                read_value = True
        return abs(change_time)


#### this is the class that will be defined as how the device will calculate the ptt\ptNorm  values
class PttNormThreadLocks(object):
   def __init__(self,l,LightSensor0,IrSensor0,LightSensor1,IrSensor1):
      self.l = l
      self.LightSensor0 = LightSensor0
      self.IrSensor0= IrSensor0
      self.LightSensor1 = LightSensor1
      self.IrSensor1 = IrSensor1

   def PttLocks(self):
      L = self.l
      L.aquire()
      Ir0=IrSensor(self.LightSensor0, self.IrSensor0)
      ir0 = Ir0.__iRDectector__()
      Ir1=IrSensor(self.LightSensor1, self.IrSensor1)
      ir1 = Ir1.__iRDectector__()
      L.release()
      return [ir0, ir1]



'''
class ptt_and_norm_reader(object):
    def __init__(self,lock,data,data1):
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
these are the four threads that I am trying to run to get any average for the individual 

def main():
   each sensor is being called

    l_sensor0 = LightSensor(24, 18)
    l_sensor1 = LightSensor(23, 17)
    # l_sensor2 = LightSensor(22,16)
    # l_sensor3 = LightSensor(25,12)
   each value of the sensor is being retuend then printed
    val_sensor0 = l_sensor0.sensor
    val_sensor1 = l_sensor1.sensor
    # val_sensor2 = l_sensor2.light_Sensor()
    # val_sensor3 = l_sensor3.light_Sensor()
   what each value is being sent to the manchine
    print(val_sensor0)
    print(val_sensor1)
    # print(val_sensor2)
    # print(val_sensor3)

    l_sensor0.reset()

if __name__ == "__main__":
     main()
this is any artifact in which I need to find out how it 
GPIO.add_event_callback(l_Sensor0 , t1)
GPIO.add_event_callback(l_Sensor1 , t2)
GPIO.add_event_callback(l_Sensor2 , t3)
GPIO.add_event_callback(l_Sensor3 , t4)
'''
