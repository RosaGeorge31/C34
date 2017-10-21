#!/bin/bash
clear
echo "Enter the name"
read f
if test -f $f
then if test -r $f 
    then if test -w $f
    then echo "$f has read write permission"
    fi
    else echo "$f does not have read write permission"
    fi
    else echo "$f not a file"
fi
    
