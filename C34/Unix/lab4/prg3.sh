#!/bin/bash
clear
echo "enter 5 elements in a single line"
read -a array 
min=${array[0]}
max=${array[0]}

for i in "${array[@]}" 
do

if [ $i -gt $max ] 
then max=$i
fi
if [ $i -lt $min ] 
then min=$i
fi
done 

for i in "${array[@]}" 
do
c=0
for j in "${array[@]}" 
do 
   if [ $i -eq $j ]
   then ((c=c+1))
   fi
done
   if [ $c -ne 1 ]
    
    then echo "$i gets repeated $c time(s)"
    fi
    ((i=i+c)) 
done
echo "Min = $min"
echo "Max = $max"
