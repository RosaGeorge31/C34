#!/bin/bash
clear
i="y"
echo "Enter name of database "
read db
while [ $i = "y" ]
do
clear
echo "1.View the Data Base "
echo "2.View Specific Records "
echo "3.Add Record "
echo "4.Delete Record "
echo "5.Exit "
echo "Enter your choice "
read ch
    case $ch in
        1)cat $db;;
        2)echo "Enter roll number "
          read roll
            grep -i "$roll" $db;;
        3)echo "Enter new roll number "
          read roll
          echo "Enter new name:"
          read name
          echo "Enter semester "
          read sem
          echo "Enter mark of subject 1"
          read m1
          echo "Enter mark of subject 2"
          read m2
          echo "Enter mark of subject 3"
          read m3
          echo "$roll    $name    $sem    $m1     $m2     $m3">>$db;;
        4)echo "Enter Roll number"
          read rno        
        grep -v "$rno" $db >dbs1    
          echo "Record is deleted"
         cat dbs1;;           
        5)exit;;
        *)echo "Invalid choice ";;
    esac
echo "Do u want to continue ?"
read i
if [ $i != "y" ]
then
    exit
fi
done         
