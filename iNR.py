#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### variables ##### 
f=open(bloodtest.ace2,'r+a')
inr = 0.0
pt = 0.0
ptnom = 0.0
isitest=0
slope=0
isiref=0
user_data_low = 0.0
user_data_high = 0.0
tester_data =0.0
a=0
b=0
c=0
i=0
#### main program #####

while(i== 1 and n==exit):

   user_data_low = input('prompt the users to enter a two digit number ')
   user_data_high = input('prompt the users to enter a two digit number ')
   f.write(user_data_low)
   f.write(user_data_high)
   while (i <= 100000 or n== reset):
      if (i<= 100000):
          n = input('if you made a mistake when input your intial values type reset.')
      if (i !=1 and n==reset):
         i=i+1
         if(i == 1 or n==reset):
            print(inr 'and' pt)
            if(n==input{'just type reset'}):
   n = input('type exit if you have or accidental wanted to restart to quit other wise it not going to prefrom a last check')
   if (n!=1 or n < 1 or  n==exit):
       print(inr 'and' pt)
   
### i got to figure out how to make INR calculation

int_nor_rat(inr):
   inr = (pt/ptnom)^isitest


### slope

slope = (a-c)/(b-c)
#### isi 

isitest = isiref*slope


### create the logirithm slope of a b and c

if(a < b ):

### slope
else:
   slope = (a-c)/(b-c)

###last one #####
if (size == 0):
f.readline(size-1)


#### writing it to a file then adding it to that and printing it out
