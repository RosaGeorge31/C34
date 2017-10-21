#!/bin/bash
echo "Enter the time "
read s
h=`echo $s| cut -c 1-2`
m=`echo $s | cut -c 4-5`
if [ $m -gt 59 ]
then
    echo "Wrong Input!"
    exit
fi
echo "Hour-$h  Min-$m"
if [ $h -le 11 ]
then echo "Good Morning!"
elif [ $h -le 17 ]
then echo "Good Afternoon"
elif [ $h -le 19 ]
then echo "Good Evening"
else
echo "Good Night"
fi


