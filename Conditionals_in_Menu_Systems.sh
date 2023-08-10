!/usr/bin/bash

#Script : Conditionals_in_Menu_Systems.sh
#Purpose: Create a bash script that launches a menu system with the following options:
############## Hello world (prints “Hello world!” to the screen)
############## Ping self (pings this computer’s loopback address)
############## IP info (print the network adapter information for this computer)
############## Exit
######### Next, the user input should be requested.
######### The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
######### Use a loop to bring up the menu again after the request has been executed.
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
