#!/bin/bash
clear
select k in home user_name today users terminal_no
do
   case $k in
   home) echo "$HOME";;
   user_name) uname -n;;
   today) d=`date +%d`
          m=`date +%m`
          y=`date +%y`
          echo "$m / $d / $y";;
   users) echo -n "NUmber of users : "
          users|wc -w;;
   terminal_no) echo -n "Terminal : "
                tty|cut -c 10-;;
   *) exit;;
   
   esac
done

   


