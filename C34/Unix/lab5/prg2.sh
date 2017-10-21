#!/bin/bash
clear
echo "Enter the name"
read f
if test -f $f
then cat<$f
elif test -d $f
then cd $f 
      ls
      cd ..  
else
echo "Wrong input"
fi
    
