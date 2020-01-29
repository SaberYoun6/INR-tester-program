#!usr/bin/env python3
#
#
#
#
#


## this will be the main test file until I have a more complete version then this will probably become the main file 
#dependenicesL
from iNR import IrSensor, PttNormThreadLocks
import socket 
from pathlib import Path
#from datasave import InitalSavedData
import stored
import os
from multiprocessing import Process, Lock
import numpy as np
#gobal varaibles
l_sensors = []
host = socket.gethostname()
paths = "/home/pi/inr/"
host_name_file= paths + host
creation_file = open(host_name_file, "w+")

def main():
   item=0
   print("checking to see if you have the file")

   #if !Path(paths):
   #    item =1 


    #   while item == 1 :
    #       print("Enter the lower range of INR")
    #       first_inr_user_value  = input()
    #       print("Enter the high range of INR")
    #       second_inr_user_value = input()
    #       first_inr_user_value  = np.longdouble(first_inr_user_value)
    #       second_inr_user_value = np.longdouble(second_inr_user_value)
    #       print("/n")
    #       print("Verifying that the data is correct %.1f , %.1f/n"% (first_inr_user_value,second_inr_user_value))
    #       creation_file.write("Verifying that the data is correct %.1f , %.1f/n"% (first_inr_user_value,second_inr_user_value))
    #       print("press 1 to continue")

   print("Entering 9 will close the program, E 0 will allow the user to change the INR levels, enter 1")
   
   item =input()
   items = int(item)

   while (items <= 9):
      

      if items == 0:
          print("Enter your new lower range for INR")
          first_inr_user_value=input()
          print("Enter your new high range for INR")
          second_inr_user_value= input()
          first_inr_user_value  = np.longdouble(first_inr_user_value)
          second_inr_user_value = np.longdouble(second_inr_user_value)
          items =input()
          items = int(item)
          ##copy method to transfer the new items over stored.py
          ## I need a way to
      elif items == 1:
          light0     = IrSensor(24,18)
          light1     = IrSensor(23,17)
          light2     = IrSensor(22,16)
          light3     = IrSensor(25,12)

          val_light0 = light0.__iRDectector__()
          val_light1 = light1.__iRDectector__()
          val_light2 = light2.__iRDectector__()
          val_light3 = light3.__iRDectector__()
          print("test: the light values v1:%.2f , v2:%.2f , v3:%.2f , v4:%.2f " %(val_light0,val_light1,val_light2,val_light3))
          items =input()
          items = int(item)
      elif items == 2 :
          light = IrSensor(24,18)
          val_light = light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          items =input()
          items = int(item)
          continue
      elif items == 3 :
          light     = IrSensor(23,17)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          items =input()
          items = int(item)
          continue
      elif items == 4 :
          light     = IrSensor(22,16)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          items =input()
          items = int(item)
          continue
      elif items == 5 :
          light     = IrSensor(25,12)
          val_light =light.__iRDectector__()
          print('testing one sensor at a time %f'%(val_light))
          items =input()
          items = int(item)
          continue
      elif items == 6 :
          lock = Lock()
          test_ptt=PttNormThreadLock(lock,24,18,23,17)

          for num in range(180):
             Process( target=PttLocks, args=test_ptt).start()
          
          items =input()
          items = int(item)
          continue

      elif (item == 7):
         light0 ,light1 ,light2 ,light3    = IrSensor(24,18), IrSensor(23,17), IrSensor(22,16), IrSensor(25,12)
         val_light0,val_light1,val_light2,val_light3 = light0.__iRDectector__(),light1.__iRDectector__(),light2.__iRDectector__(),light3.__iRDectector__()
         print("V0: %.2f, V1: %.2f, V2: %.2f, V3: %.2f" %(val_light0,val_light1,val_light2,val_light3))
         items =input()
         items = int(item)
         continue
      elif(item ==8): 
         print("foo")
      elif(item == 9):
         print("closing programing")
         break
      else:
         print("You've gone above the numers that I was think")
         break

   print("closing program")



main()
