#!/usr/bin/env python3
#
#
#
# Create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.
# This is going to be used for to get the initial results for the INR ratio. then it'll be called again to figure out
# what is going on.
#    Please elaborate on what you mean by "figure out what is going on" - Justin
# 
#
__author__ = "Samuel Young"
__copyright__ =" Copyright 2016, The INR project"
__credits__ = ["Samuel Young"]
__license__ = "GPL"
__version__ = "0.0.7"
__maintainer__= "Samuel Young"
__email__ = "samuel.young.103@gmail.com"
__status__ = "beta"
#### dependencies ##### 

#import RPi.GPIO as GPIO
import time
import threading

#### variables ####
#ptdrawc2= input('INR')
#ptnomdrawc2= int(ptdrawc2)
##### #GPIO  #######
#GPIO.setmode(#GPIO.BCM)
#GPIO.setwarnings(False)



class LightSensor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection= reflection


    @staticmethod
    def reset():
        """
        NOTE : README This does not need to be a member method, as I believe that
        #GPIO is reset all at once and not on an individual level.
        :return: boolean
        """
       ##GPIO.cleanup() # commenting because I am not doing this on a Pi and I'm tired of errors.
       print("Gpio Cleanup has been done")


    def light_sensor(self):
        count = 0
        delta_time = 0.0
        global value
        value = False
        print("setting up  pins")
        #GPIO.setup(self.reflection, #GPIO.OUT)
        #GPIO.output(self.reflection,#GPIO.LOW)
        #GPIO.setup(self.light,#GPIO.OUT)
        ##led_off= #GPIO.output(self.light,#GPIO.LOW)
        #time.sleep(7.5)
        print("testing light")
        #led_on=#GPIO.output(self.light,#GPIO.HIGH)
        time.sleep(1)
        print("Setup the input pin")
        #GPIO.setup(self.reflection,#GPIO.IN)
        init_time= time.perf_counter()
        timer1=time.time()
        # TODO This is currently an infinite loop. value needs to be set to False at some point to terminate loop.
        # I am commenting this out for now.
        # nvm missed the breaks. If value is unnecessary, remove it.
        """while 1  or  value == True:
            #refc= #GPIO.input(self.reflection)
            #led_on
            time.sleep(.0000001)
            final_time = time.perf_counter()
            timer2 = time.time()
            count = count + 1
            if refc == 0:
               #led_on
               timer2=time.time()
               if count == 359901:
                   value = True
                   delta_time = final_time - init_time
                   #GPIO.output(self.light,#GPIO.LOW)
                   break
            elif .01 <= refc <= .99:
               #led_on
               time.sleep(.000001)
               if count == 359901:
                   value = True
                   delta_time = final_time - init_time
                   #GPIO.output(self.light,#GPIO.LOW)
                   break
            else: 
               #GPIO.output(self.light,#GPIO.LOW)
               value = True
               delta_time = final_time - init_time
               break
               """
        return delta_time


class PttAndNormReader(object):
    """
    This class calculates ptt\ptNorm values
    """
    def __init__(self, light, reflection):
        self.light = light
        self.reflection = reflection

    def ptt_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print(" PTT LightSenors array in use")
        light_sensor=l_sensor.light_sensor()
        l_sensor.reset()
        return light_sensor

    def norm_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print("Norm LightSenors array in use")
        light_sensor=l_sensor.light_sensor()
        l_sensor.reset()
        return light_sensor

    def ptt_reader(self):
        ask = 0 
        pt_drawing = self.ptt_draw()
        for i in pt_drawing:
            ask=i
        return pt_drawing

    def norm_reader(self):
        ask = 0
        norm_drawing = self.norm_draw()
        for i in norm_drawing:
            ask=i
        return norm_drawing

# Example of how to do the threaded stuff.
ptt_t0_object = LightSensor(24, 18)
ptt_t0  = threading.Thread(target = ptt_t0_object.light_sensor)

norm_t0 = threading.Thread(target = LightSensor.light_sensor, args=(23,17))
ptt_t1  = threading.Thread(target = LightSensor.light_sensor, args=(22,16))
norm_t1 = threading.Thread(target = LightSensor.light_sensor, args=(25,12))

# Locks would go around any access to shared variables. This is unnecessary.
class lightSensor_threading:
     def locking_lightSensor():
         r_lock = threading.Rlock()

       
def main():
    # TODO Fix the variable names and make them consistent.
   val_sensor0 = l_sensor0.light_Sensor()
   val_sensor1 = l_sensor1.light_Sensor()
   val_sensor2 = l_sensor2.light_Sensor()
   val_sensor3 = l_sensor3.light_Sensor()
   print(val_sensor0)
   print(val_sensor1)
   print(val_sensor2)
   print(val_sensor3)

if __name__ == "___main___":
    main()

    l_Sensor0=0
    l_Sensor1=0
    l_Sensor2=0
    l_Sensor3=0


#GPIO.add_event_callback(l_Sensor0 , t1)
#GPIO.add_event_callback(l_Sensor1 , t2)
#GPIO.add_event_callback(l_Sensor2 , t3)
#GPIO.add_event_callback(l_Sensor3 , t4)



l_sensor0.reset()
l_sensor1.reset()
l_sensor2.reset()
l_sensor3.reset()
