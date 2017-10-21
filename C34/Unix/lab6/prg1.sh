#!/bin/bash
echo "Enter the number of people: "
read n

for (( i = 1; i<= n ; i++ ))
do
echo "Enter name and address"
read name
read add
echo "$name    $add" >>address.lst

done
echo "Names    Address"
cat < address.lst
