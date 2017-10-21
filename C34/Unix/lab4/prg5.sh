#!/bin/bash
clear
for(( i=1;i<=999;i++ ))
do
    tmp=$i
    s=0
    while [ $tmp -ne 0 ]
    do
        ((d=tmp%10))
        ((s=s + (d*d*d)))
        ((tmp=tmp/10))
    done
    if [ $s -eq $i ]
    then    echo $s
    fi
done
    
