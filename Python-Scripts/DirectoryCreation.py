#!/usr/bin/python3

# Import libraries
import os
import subprocess

#Script : DirectoryCreation.py
#Purpose: Script must ask the user for a file path and read a user input string into a variable.
######### Script must use the os.walk() function from the os library.
######### Script must enclose the os.walk() function within a python function that hands it the user input file path.
#Why    : Understand how to create directories with os.makedirs() and how to walk through dirs with os.walk()


#Function name: create_directories
#Purpose      : Takes a user input string
#               Creates a directory named the string using os.makdirs function
#               Create sub-directories within the directory named 'string_01', 'string_02', and 'string_03'     
def create_directories():
    
    ### Directory's creation
    ### Do not raise an error if the directory already exists 
    os.makedirs(path,exist_ok=True)
    
    ### Sub-Directories' declaration
    sub_directories = [f"{user_in}_01", f"{user_in}_02", f"{user_in}_03"]
    
    ### Sub-Directories' creation
    for subdirs in sub_directories:
        os.makedirs(f"{path}/{subdirs}",exist_ok=True)
    
 
#Function name: create_directories
#Purpose      : Takes a user input string
#               Creates a directory named the string using os.makdirs function
#               Create sub-directories within the directory named 'string_01', 'string_02', and 'string_03'   
def output_2_file(path):
    with open("output.txt","a") as f:
        for (root, dirs, files) in os.walk(path, topdown=True):
            ### ==root==
            f.write(root + "\n")
            #print(root + "\n")
            
            
            ### ==dirs==
            for name in dirs:
                f.write(os.path.join(root, name) + "\n")
                #print(os.path.join(root,name) + "\n")

            ### ==files==        
            for name in files:
                f.write(os.path.join(root, name) + "\n")
                #print(os.path.join(root,name) + "\n")
   
            
            



# Main

### Read user input here into a variable
user_in = input("Enter the directory's name:")
    
### The directory will be created in the current directory
parent_dir = "."
path = os.path.join(parent_dir,user_in)    
    
    
create_directories()

output_2_file(path)


########## It is also necessary to open the .txt file with Libre Office Writer ##########
##########        Need to review the openning of the library office            ##########

subprocess.run(["libreoffice", "--view", "file_list.txt"])

# End
