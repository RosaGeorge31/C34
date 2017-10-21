#!/bin/bash
clear
echo "Enter the Unix marks"
read m1
echo "Enter the Java marks"
read m2
echo "Enter the Dsa marks"
read m3
((tot= $m1+$m2+$m3))
av=$(echo "scale=0; $tot / 3"|bc)
#av=$(python -c "print $tot / 3")
echo "Avg = $av"
if test $av -ge 70
then echo "Distinction"
    exit
fi
if test $av -ge 60
then echo "First Class"
exit
fi
if test $av -ge 50
then echo "Second Class"
exit
fi
if test $av -ge 40
then echo "Third Class"
exit
fi

echo "Fail"



