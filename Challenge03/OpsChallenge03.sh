#!/usr/bin/bash

#Script : OpsChallenge03.sh
#Purpose: Change permissions of a directory received by the user
#Why    : To show some skills with permissions 



#Funtion name: quit
#Purpose     : exit the program if the user want to
quit() {

        if [[ $1 == "q" ]]
        then
                echo -e $(date +'[%Y-%m-%d T %H:%M:%S]') User asked for quit the script"\n" >> $log_file
                echo -e $(date +'[%Y-%m-%d T %H:%M:%S]') Ending script OpsChallenge03.sh >> $log_file
                echo -e Exiting...
                exit 0
        fi

}

#Function name: change_permissions
#Purpose      : change the specified permissions of all file of the specified directory
change_permissions() {
        echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') In function change_permissions()\n" >> $log_file

        cd  "$(eval echo "$1")"
        echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Change directory to $(eval echo "$1")\n" >> $log_file

        #saves in a local variable the files
        local listFiles=$(ls)

        #saves the info about the files before modifications 
        before_modifications=$(ls -l)

        echo -e "\n\n"
        for f in * 
        do
                chmod "$2" $f
                echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Change permissions in file $f\n" >> $log_file 
                echo -e "File $f was changed\n"
                sleep 1
        done

        #saves the info about the files after modifications
        after_modifications=$(ls -l)

        echo -e "\n\n------>Before changing permissions:\n $before_modifications"
        echo -e "\n\n------>After changing permissions:\n $after_modifications"

        echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Display the information about Files in $(eval echo "$1") directory\n" >> $log_file 

        cd "$current_directory"
        echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Change directory to $current_directory\n" >> $log_file
}




questions=($'Give me the directory path you want to change the permissions! (press \"q\" to exit)\n>' 
        $'Give me the permissions number! (press \"q\" to exit)\n>')

variables=(directory_path permissions_number)

current_directory="$(pwd)"
log_file="$current_directory/logs"



#overwrite if file exists
echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Starting script OpsChallenge03.sh\n" > $log_file
echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') In main\n" >> $log_file 


for i in 0 1
do 

        read -p  "${questions[i]}" ${variables[i]}
        echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') $((i+1)) question and $((i+1)) responde performed\n" >> $log_file
        quit "${!variables[i]}"

done

change_permissions "${!variables[0]}" "${!variables[1]}"

echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') In main\n" >> $log_file
echo -e "$(date +'[%Y-%m-%d T %H:%M:%S]') Ending script OpsChallenge03.sh" >> $log_file
