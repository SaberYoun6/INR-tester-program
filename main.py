#!usr/bin/env python3


## this will be the main test file until I have a more complete version then this will probably become the main file 
#dependenices
from iNR import LightSensor
import socket 
import pathlib
import datasave
import stored
import numpy as np
#gobal varaibles
l_sensors = []
host = socket.gethostname():

creationfile = open('~/' + host,"r")

def main():
   print("")

   if !(pathlib.path("~/"+ host): 
         while item == 1 :
             first_inr = input()
             print("/n")
             second_inr = input()
             first_inrfl=np.float128(first_inr)

             second_inrfl=np.float128(second_inr)
             print("/n")
             initalSavedData.user_input(first_inr,second_inr)
             print("verifing that the data is correct %.1f , %.1f",first_inr,second_inr)
             print("press 1 to continue")
             item =input()
             item = int(item)
   else:
          continue
   item = input()
   item =int(item)

   while (item == 9):
      if item == 0:


      else if (item == 7):
         light     = LightSensor(24,18)
         val_light = light.sensor()
         print(val_light)
         light.reset()
      print()
      item = input()
      item = int(item)

   





main()
