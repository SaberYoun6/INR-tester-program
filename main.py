#!usr/bin/env python3
#
#
#
#
#


## this will be the main test file until I have a more complete version then this will probably become the main file 
#dependenices
from iNR import IrSensor
import socket 
import pathlib
from datasave import InitalSavedData
import stored
import numpy as np
#gobal varaibles
l_sensors = []
host = socket.gethostname()
host_name_file= "~/inr/" + host
creation_file = open(shots, "r+")

def main():
   print("checking to see if you have the file")

   if  pathlib.path(host_name_file):
      while item == 1 :
          print("Enter the lower range of INR")
          first_inr_user_value  = input()
          print("Enter the high range of INR")
          second_inr_user_value = input()
          first_inr_user_value  = np.float128(first_inr_user_value)
          second_inr_user_value = np.float128(second_inr_user_value)
          print("/n")
          print("Verifying that the data is correct %.1f , %.1f",first_inr_user_value,second_inr_user_value)
          print("press 1 to continue")
          InitalSaveData(creation_file)
          initalSavedData.user_input(first_inr_user_value,second_inr_user_value)
          item =input()
          item = int(item)
   else:
        continue
   item = input()
   item =int(item)

   while (item == 9):
      if item == 0:
          print("Enter your new lower range for INR")
          first_inr_user_value=input()
          print("Enter your new high range for INR")
          second_inr_user_value= input()
          ##copy method to transfer the new items over stored.py
          ## I need a way to



      elif (item == 7):
         light     = IrSensor(24,18)
         val_light = light.__iRDectector__()
         print(val_light)
      print()
      item = input()
      item = int(item)


    print("closing program")






main()
