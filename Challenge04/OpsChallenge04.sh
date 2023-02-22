#!/usr/bin/bash

#Script : OpsChallenge04.sh
#Purpose: Make a user interation menu
#Why    : To practice Bash conditional statement




while [ 1 ] 
do
        # Options
        echo -e "Available options:\n"
        echo -e "\t1) Prints Hello World (ex.: \"Hello world!\")\n"
        echo -e "\t2) Ping self\n"
        echo -e "\t3) Ip info\n"
        echo -e "\t*) Exit\n"


        read -p "Select your option:" opt

        echo "-----------------------------------------------"
        case $opt in
                "1") echo -e "\n > Hello world!\n" ;;
                "2") echo -e "\n" 
                       ping -c 4 127.0.0.1
                       echo -e "\n"             ;;
                "3") echo -e "\n"
                        ip a
                        echo -e "\n"            ;;
                  *) exit 0                     ;;  
        esac
        echo "-----------------------------------------------"
done