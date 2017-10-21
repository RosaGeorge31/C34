#!/bin/bash
clear
echo "enter 10 elements in a single line"
c_n=0
c_p=0
c=0
read -a arr 

for i in "${arr[@]}" 
do
    if [ $i -gt 0 ] 
    then ((c_p = c_p + 1))
    fi
    
    if [ $i -lt 0 ] 
    then ((c_n= c_n + 1))
    fi
    if [ $i -eq 0 ] 
    then ((c = c + 1))
    fi
done

for(( i=0;i<10;i++ ))
do
   for(( j=0;j<9;j++ )) 
    do
    if [ ${arr[$j]} -gt ${arr[$((j+1))]} ] 
    then tmp=${arr[$j]}
         arr[$j]=${arr[$((j+1))]}
         arr[$((j+1))]=$tmp
    fi
  done
done
echo "ascending order:"
for i in "${arr[@]}" 
do
    echo $i
done

echo "Number of positive and negative numbers are $c_p and $c_n respectively"

echo "NUmber of zeroes = $c"


