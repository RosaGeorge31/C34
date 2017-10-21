#!/bin/bash
clear
echo "Enter the first file name"
read f1
echo "Enter the second file name"
read f2
if test -f $f1  
then if test -f $f2 
   then echo "File 1 and file 2 are present"
        cat $f1| cat >> $f2   
        cat < $f2
   else
   echo "File 2 not present"
fi
else echo "Both files not present"
fi
