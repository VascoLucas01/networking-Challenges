#!/usr/bin/bash

#######################IMPORTANT NOTE##############################
#due to permissions the script needs to be executed by a super user
###################################################################

#Script : Clearing_Logs.sh
#Purpose: Print to the screen the file size of the log files before compression
######### Compress the contents of the log files listed below to a backup directory
############### /var/log/syslog
############### /var/log/wtmp
######### The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
###############Example: /var/log/backups/syslog-20220928081457.zip
######### Clear the contents of the log file
######### Print to screen the file size of the compressed file
######### Compare the size of the compressed files to the size of the original log files
#Why    : To understand the importance of clearing log files.

################################# IMPORTANT NOTE #################################
### Clearing the tracks is the final stage of penetration testing process
### Clearing tracks essencially involves clearing all the activity of an attacker
### From the attackers' perspective: they usually need to evade detection
# if there is an intrusion detection system. Therefore preventing any incident
# response, they need to clear the logs or back doors that can be discovered 
# by forensics team
##################################################################################

log_files=("syslog  file: " "wtmp    file: "  "authlog file: " "boot 1  file: " "boot 2  file: " "kernel  file: ")  
log_files_path=("/var/log/syslog" "/var/log/wtmp" "/var/log/auth.log" "/var/log/boot.log.1" "/var/log/boot.log.2" "/var/log/kern.log")
zip_log_files_path=("/var/log/backups/syslog-" "/var/log/backups/wtmp-" "/var/log/backups/auth.log-" "/var/log/backups/boot.log.1-"
"/var/log/backups/boot.log.2-" "/var/log/backups/kern.log-")
zip_log_files=("syslog  file zip: " "wtmp    file zip: " "authlog file zip: " "boot 1  file zip: " "boot 2  file zip: " "kernel  file zip: ")

#eventually if the dir was removed or moved
if [ ! -d /var/log/backups ]
then

        mkdir /var/log/backups

        #change the user permissions to be possible to compress to that directory, however it is not necessary in this case
        #sudo chown -R $(whoami) /var/log/backups

fi



for (( i=0; i<${#log_files[@]}; i++ ))
do
	size=$(stat -c %s ${log_files_path[i]})
	echo -e "\t> ${log_files[i]} $size"

	date_tmp=$(date +'%Y%m%d%H%M%S')
	zip -q "${zip_log_files_path[i]}$date_tmp.zip" "${log_files_path[i]}"
	zip_size=$(stat -c %s ${zip_log_files_path[i]}$date_tmp.zip)
	echo -e "\t> ${zip_log_files[i]} $zip_size"

	echo -e "(${log_files[i]%??}) - (${zip_log_files[i]%??}) = $(($size-$zip_size))"
	bash -c "> ${log_files_path[i]}"

	echo ""
done
