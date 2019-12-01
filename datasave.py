## Samuel Young
## GNU 3 
## So i want this file to encrypt the information before I send it to the files and I want a a key to be used to insure that no one can have access to the files because this insure the security of subjects to read from the current on and move that data to from a file called iNR.py and move it onto another file..
#!/usr/bin/env python3 
import datetime
import sys
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, MultiFernet 
from cryptography.hazmat.primitives import serilization
from cryptography.hazmat.primities.serilization import load_pem_private_key
from cryptography.hazmat.primities.assymmetric import rsa
import socket
from stored import storage

###variable ###
host = socket.gethostname()
encrypteddict = {}
f= MultiFernet(key,key2,key3)






###intial setup of files

class initalSavedData(object):
   def __init__(self , creationfile = host, ):
      self.creationfile =creationfile
   def initial_input(self,number,number1):
      f = open("~/inr/.",self.creationfile,"w+")
       = self.informationFile()
      f.write("%s\n %.1f,%.1f\n"%(f.encrypt(creationfile),f.encrypt(number),f.encrypt(number1)))
      f.close()
   def intial_test(self,value1,value2,value3,value4):
      encrypteddict[f.encrypt(datatime.date)]=f.encrypt(value1)
      encrypteddict[f.encrypt(datatime.date)]=f.encrypt(value2)
      '''
      encrpteddict[datatime.date]=value3
      encrpteddict[datatime.time]=value4
      '''
      f= open("~/inr/.",self.creationfile,"a+")

      f.write("encrypteddict")
   def read_encodevalues(encrypteddict):
      try: 
         f= open("~/inr/.",self.creationfile,"r")
         f.read()
      except FileNotFoundError a:
         print("File wasn't created")
      finally:
         
       for k,i in range(len(encrypteddict)i):
           print("%s,%s " %(f.decrypt(k),f.decrypt(i)))




       
      







### encryption ### 
  
class information_file(object):
   def __init__(self, file0 ="pem1.key:",file1="pem0.key"):
      self.file0=file0
      self.file1=file1
   def encryption():


### decryption ###



### key that holds that hands ###



### the key generater #####

class generator(object):
   def __init__(self, file0= "pem1.key",file1="pem0.key"):
      self.file0 = file0
      self.file1 = file1
   def save_key(self, pk , pk1 ):
      salt= os.urandom(32)
      pem1= pk.private_bytes(
            encoding=serilization.Encoding.PEM,
            format=serilization.PrivateFormat.TraditionalOpenssl,
            ecryption_algorithm= hashes.SHA3_512()
            salt= salt
            length= 64
            iteration=100000
      )
      with open(self.file0, 'wb') as pem1_out
           pemt_out.write(pem1)
      pem0= pk1.private_bytes(
            encoding=serilization.Encoding.PEM,
            format=serilization.PrivateFormat.TraditionalOpenssl,
            ecryption_algorithm= hashes.SHA3_512()
            salt= salt
            length= 64
            iteration=100000
      )
      with open(self.file0, 'wb') as pem0_out
           pemt_out.write(pem)

   def gen_key(self):
      private_key = rsa.generate_private_key(
            public_exponent=65537, key_size= 4096, backend=default_backend()
            )
      return private_key
   def load_key(self):
      with open(self.file0, 'rb') as pem_in:
         premlines = pem_in.read()
      private_key  = load_pem_private_key(pemlines,none,default_backend())
      with open(self.file1, 'rb') as pem0_in:
         pem0lines = pem0_in.read()
      private_key1 = load_pem_private_key(pem0lines, None, default_backend())

   
      return (private_key ,private_key1)

   def setup_keys(self)
   dirName="~/inr/.keys/"
   if not os.path.exists(dirName)
      os.mkdir(dirName)
      print("Directory , %s , created "%(dirName))
      os.chdir(dirName)
      pk0= self.gen_key()
      pk1= self.gen_key()
      self.save_key(pk0,pk1)


   else:
      print("Directory exists") 

### the encoding to files ###



### the encoding out of the files ###
