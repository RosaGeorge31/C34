#!/bin/bash
echo "Enter the first number"
read n1
echo "Enter the second number"
read n2
i="y"
while [ $i = "y" ]
do
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "Enter your choice"
read ch
case $ch in 
1)sum=`expr $n1 + $n2`
echo "Sum = $sum";;
2)d=`expr $n1 - $n2`
echo "Difference = $d";;
3)mul=`expr $n1 \* $n2`
echo "Multiplication = $mul";;
4)div=$(echo "scale=3; $n1 / $n2"|bc)
echo "Division = $div";;
*)echo "Invalid Choice";;
esac
echo "Do you want to continue?(y/n)"
read i
done
echo "End"

