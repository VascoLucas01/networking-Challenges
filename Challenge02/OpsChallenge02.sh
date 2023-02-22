#!/usr/bin/bash

#Script : OpsChallenge02.sh
#Purpose: Make a backup of the log messages
#Why    : To show some skills in file management 


filename="logMessages.BACKUP"


# the script initial message
echo -e "\n$(date +'[%Y-%m-%d T %H:%M:%S]') Script is starting...\n" 


# make a backup of the log messages to the filename
echo -e "\n\n$(journalctl --no-pager )" > $filename
echo -e "\n\n$(date +'[%Y-%m-%d T %H:%M:%S]')" >> $filename 

# print the message that tells the success of the backup
echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') The backup was a success!"
