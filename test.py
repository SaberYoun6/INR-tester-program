#!usr/bin/env python3


## this will be the main test file until I have a more complete version then this will probably become the main file 
#dependenices
from iNR import LightSensor
#gobal varaibles
l_sensors = []

def main():
   light     = LightSensor(24,18)
   val_light = light.sensor()
   print(val_light)
   light.reset()





main()
