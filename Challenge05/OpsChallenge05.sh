#!/usr/bin/bash

#IMPORTANT NOTE
#due to permissions the script needs to be executed by a super user


#Script : OpsChallenge05.sh
#Purpose: Not removing log files from the system, but just clearing it.
#Why    : To understand the importance of clearing log files.



syslog_size=$(stat -c %s "/var/log/syslog")
wtmp_size=$(stat -c %s "/var/log/wtmp")
auth_size=$(stat -c %s "/var/log/auth.log")
boot_1_size=$(stat -c %s "/var/log/boot.log.1")
boot_2_size=$(stat -c %s "/var/log/boot.log.2")
kernel_size=$(stat -c %s "/var/log/kern.log")

echo -e "\nThe size in bytes of the log files are:"
echo -e "\t> syslog  file: $syslog_size"
echo -e "\t> wtmp    file: $wtmp_size"
echo -e "\t> authlog file: $auth_size"
echo -e "\t> boot 1  file: $boot_1_size"
echo -e "\t> boot 2  file: $boot_2_size"
echo -e "\t> kernel  file: $kernel_size"




#eventually if the dir was removed or moved
if [ ! -d /var/log/backups ]
then

	mkdir /var/log/backups

	#change the user permissions to be possible to compress to that directory, however it is not necessary in this case 
	#sudo chown -R $(whoami) /var/log/backups

fi


syslog_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/syslog-$syslog_date.zip" "/var/log/syslog"

wtmp_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/wtmp-$wtmp_date.zip" "/var/log/wtmp"

auth_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/auth.log-$auth_date.zip" "/var/log/auth.log"

boot_1_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/boot.log.1-$boot_1_date.zip" "/var/log/boot.log.1"

boot_2_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/boot.log.2-$boot_2_date.zip" "/var/log/boot.log.2"

kernel_date=$(date +'%Y%m%d%H%M%S')
zip -q "/var/log/backups/kern.log-$kernel_date.zip" "/var/log/kern.log"

bash -c "> /var/log/syslog"
bash -c "> /var/log/wtmp"
bash -c "> /var/log/auth.log"
bash -c "> /var/log/boot.log.1"
bash -c "> /var/log/boot.log.2"
bash -c "> /var/log/kern.log"


syslog_zip_size=$(stat -c %s "/var/log/backups/syslog-$syslog_date.zip")
wtmp_zip_size=$(stat -c %s "/var/log/backups/wtmp-$wtmp_date.zip")
auth_zip_size=$(stat -c %s "/var/log/backups/auth.log-$auth_date.zip")
boot_1_zip_size=$(stat -c %s "/var/log/backups/boot.log.1-$boot_1_date.zip")
boot_2_zip_size=$(stat -c %s "/var/log/backups/boot.log.2-$boot_2_date.zip")
kernel_zip_size=$(stat -c %s "/var/log/backups/kern.log-$kernel_date.zip")

echo -e "\nThe size in bytes of the log files compressed are:"
echo -e "\t> syslog file: $syslog_zip_size"
echo -e "\t> wtmp   file: $wtmp_zip_size"
echo -e "\t> authlog file: $auth_zip_size"
echo -e "\t> boot 1  file: $boot_1_zip_size"
echo -e "\t> boot 2  file: $boot_2_zip_size"
echo -e "\t> kernel  file: $kernel_zip_size"

echo -e "\nsyslog file - syslog zip file = $(($syslog_size-$syslog_zip_size))" 
echo -e "wtmp file - wtmp zip file = $(($wtmp_size-$wtmp_zip_size))" 
echo -e "authlog file - authlog zip file = $(($auth_size-$auth_zip_size))"
echo -e "boot 1 log file - boot 1 log zip file = $(($boot_1_size-$boot_1_zip_size))"
echo -e "boot 2 log file - boot 2 log zip file = $(($boot_2_size-$boot_2_zip_size))"
echo -e "kernel log file - kernel log zip file = $(($kernel_size-$kernel_zip_size))"