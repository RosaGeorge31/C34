#!/bin/bash


echo "Enter s"
read s
len=`echo ${#s}`

while [ $len -ne 0 ]
do
    r=$r`echo $s| cut -c $len`
    ((len--))
done
if test "$r" == "$s"
then echo "p"
else
    echo "np"
fi
