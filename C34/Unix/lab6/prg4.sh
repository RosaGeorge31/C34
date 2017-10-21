#!/bin/bash
clear

for(( i = 1; i <=4 ;i++ ))
do
    
        c=$i
        for((k = 1; k<= i; k++))
        do
           echo -n "$c "
           ((c=c+1))
        done
        ((c=c-1))
        for((k=1; k<=(i-1); k++))
        do
            ((c=c-1))
            echo -n "$c "     
        done
        
    echo ""
done

