#!/bin/bash/python

###is to try and create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood.

#### variables ##### 


f=open(~/Documents/bloodtest,'r+a')
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
            print(inr+' and '+  pt)
            if(n==input('just type reset')):
                n = input('type exit if you have or accidental wanted to restart to quit other wise it not going to prefrom a last check')
   if (n!=1 or n < 1 and  n==exit):
      print(inr+" and "+  pt)
   
### i got to figure out how to make INR calculation
class int_nom_rat:
   def int_nom_ratio(self):
     inr = (pt/ptnom)^isitest
	 if (inr < user_data_low):
		return (inr + "your level are to low")
	 elif (user_data_low <= inr and inr <= user_data_high):
	    return(inr + your levels are right on)
	 else:
		return(inr + your level are to high)

#### isi 

isitest = isiref*slope


### create the logirithm slope of a b and c

### slope
class detla:
   def ___A__B___C(self):
     if(a < b ):
        return
     else:
         slope = (a-c)/(b-c)

###last one #####
class final:
   def searching__the_last(self):
     if (size == 0):
        return
     else:
        f.readline(size-1)


#### writing it to a file then adding it to that and printing it out
