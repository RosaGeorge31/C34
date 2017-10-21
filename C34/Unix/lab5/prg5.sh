#!/bin/bash
clear
echo "Enter file name"
read f
if test -f $f
then ls -l $f| cut -c 2-4 |cat > s.txt
cat s.txt

fi

