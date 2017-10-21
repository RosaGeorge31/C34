#!/bin/bash
clear
echo "Enter the no of rows"
read r1
echo "Enter the no of columns"
read c1
echo "Enter the values of matrix 1 "
declare -A a
for((i=0;i<r1;i++))
do
    for((j=0;j<c1;j++))
    do
        read t
        a[$i,$j]=$t
    done
done

echo "First matrix:"
for((i=0;i<r1;i++))
do
    for((j=0;j<c1;j++))
    do
        echo -n "${a[$i,$j]}  "
    done
    echo ""
done
echo "Enter the no of rows"
read r2
echo "Enter the no of columns"
read c2
echo "Enter the values of matrix 1 "
declare -A b


for((i=0;i<r2;i++))
do
    for((j=0;j<c2;j++))
    do
        read t
        b[$i,$j]=$t
    done
done

echo "Second matrix:"
for((i=0;i<r2;i++))
do
    for((j=0;j<c2;j++))
    do
        echo -n "${b[$i,$j]}  "
    done
    echo ""
done

declare -A c
if [[ ( r1==r2 ) && (c1==c2) ]]
then
    for((i=0;i<r1;i++))
    do
        for((j=0;j<c2;j++))
        do
            sum=0
            for((k=0;k<r2;k++))
            do
                ((sum = sum + a[$i,$k] * b[$k,$j] ))
            done

        c[$i,$j]=$sum
        done
    done
 
echo "Third matrix:"
for((i=0;i<r2;i++))
do
    for((j=0;j<c2;j++))
    do
        echo -n "${c[$i,$j]}  "
    done
    echo ""
done
else
    echo "Wrong input!"
    fi
