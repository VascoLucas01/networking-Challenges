#!/usr/bin/bash

#Script : Backup_Log_Messages.sh
#Purpose: Copies /var/log/syslog to the current working directory
######### Appends the current date and time to the filename
#Why    : To show some skills in file management


filename="syslog.$(date +'[%d-%m-%Y_%H:%M:%S]')"


# the script initial message
echo -e "\n$(date +'[%Y-%m-%d T %H:%M:%S]') Script is starting...\n"


# make a backup of the log messages to the filename
journalctl --no-pager | cp /dev/stdin $filename

# print the message that tells the success of the backup
echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') The backup was a success!"
