#!/bin/bash
clear
a=$1
b=$2

while [[ ( $a -le 0 ) || ( $b -le 0 ) ]]
do    echo "Negative number present!"
        echo "Enter two positive numbers"
        read a
        read b
done
if [[ $a -gt $b ]]
then    mi=$b
        b=$a
        a=$mi
fi             
echo -n "Answer : "
echo "scale =3; $a / $b"|bc
