#!/bin/sh/ 
#Samuel Young 
#
#
RET =0	
SOUND = $(zenity --list --width=350 --height=250 --radiolist \ 
   --title = "choose the Audio Output "\
   --column "Select" --column="Output" TRUE "Leave as is" FALSE "Auto" FALSE "Force Headphones" FALSE "Force HDMI")
RET=$?
echo $SOUND 
if ["$SOUND" = "leasve as is"]; then
   amixer -c 0 cset numid=3 0
   echo "Auto set"
elif ["$SOUND" = "Force Headphones"]; then 
   amixer -c 0 cset numid=3 1
   echo "Headphones set"
elif["$SOUND"="Force HDMI" ]; then
   amixer -c 0 cset numid=3 2
   echo "HDMI set"
else
   echo "cancel"
fi

while [$RET -eq 0]; do 
   INR_tester=$(zenity --width=350 --height=700 --list \
	  --title="Choose the Following optinion" \
	  --text="INR-tester option by Samuel young."

      --column="Script name " --column="Description"\
	  iNR "it used to test the actual INR " \
	  main "its any intermedate step " \
	  datasave "this is used to save the data point " \
    RET=$?
   echo $RET
   if [ "$RET" -eq 0]
   then
	  if [ "$INR_tester" !=  ""]; then
		 cd /home/$USER/INR-tester-program
		 python $INR_tester.py
	  fi
   fi
fi
done
