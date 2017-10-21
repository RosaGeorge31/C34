#!/bin/bash
echo "Enter the number of numbers"
read n
sum=0
for((i=1; i<=$n;i++))
do
echo "Enter a number"
read val
sum=$(echo "$val + $sum"|bc)
done

div=$(echo "scale=3; $sum / $n"|bc)
echo "Average = $div"

