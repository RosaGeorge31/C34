#!/bin/bash
echo "Enter the number of numbers"
read n
sum=0
for((i=1;i<=$n;i++))
do
sum=$(echo "$sum + $i"|bc)
done
echo "The sum is $sum"
