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

   if !pathlib.path(host_name_file):
      while item == 1 :
          print("Enter the lower range of INR")
          first_inr_user_value  = input()
          print("Enter the high range of INR")
          second_inr_user_value = input()
          first_inr_user_value  = np.float128(first_inr_user_value)
          second_inr_user_value = np.float128(second_inr_user_value)
          print("/n")
          print("Verifying that the data is correct %.1f , %.1f/n",first_inr_user_value,second_inr_user_value)
          print("press 1 to continue")
          InitalSaveData(creation_file)
          initalSavedData.user_input(first_inr_user_value,second_inr_user_value)
          print("Entering 9 will close the program, E 0 will allow the user to change the INR levels, enter 1")
          item =input()
          item = int(item)
   else:
        continue
   print("Entering 9 will close the program.\n Enter 0 will allow the user to change the INR levels it will test throught. \n Enter 1 testing the light sensors. \n")
   item = input()
   item =int(item)

   while (item == 9):
      

      if item == 0:
          print("Enter your new lower range for INR")
          first_inr_user_value=input()
          print("Enter your new high range for INR")
          second_inr_user_value= input()
          first_inr_user_value  = np.float128(first_inr_user_value)
          second_inr_user_value = np.float128(second_inr_user_value)
          ##copy method to transfer the new items over stored.py
          ## I need a way to
       elif item == 1:
          light0     = IrSensor(24,18)
          light1     = IrSensor(23,17)
          light2     = IrSensor(22,16)
          light3     = IrSensor(25,12)

          val_light0 = light0.__iRDectector__()
          val_light1 = light1.__iRDectector__()
          val_light2 = light2.__iRDectector__()
          val_light3 = light3.__iRDectector__()
          print("test: the light values v1:%.2f , v2:%.2f , v3:%.2f , v4:%.2f " %(val_light0,val_light1,val_light2,val_light3))
       elif item ==2:
          light = IrSensor(24,18)
          val_light = light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          continue
       elif item ==3:
          light     = IrSensor(23,17)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          continue
       elif item ==4:
          light     = IrSensor(22,16)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          continue
       elif item ==5:
          light     = IrSensor(25,12)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          continue
       elif item ==6:
          continue
       elif (item == 7):
         light0 ,light1 ,light2 ,light3    = IrSensor(24,18), IrSensor(23,17), IrSensor(22,16), IrSensor(25,12)
         val_light0,val_light1,val_light2,val_light3 = light0.__iRDectector__(),light1.__iRDectector__(),light2.__iRDectector__(),light3.__iRDectector__()
         print("V0: %.2f, V1: %.2f, V2: %.2f, V3: %.2f" %(val_light0,val_light1,val_light2,val_light3))
         
      elif(item ==8):
         continue
      else:
         print("closing program")
      item = int(item)
      item = input()
   print("cloing program")



main()
