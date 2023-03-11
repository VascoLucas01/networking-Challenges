#!/usr/bin/python3

import subprocess

#Script : OpsChallenge10.py
#Purpose: Practice python skills
#Why    : Understand how to work with files

# creation of the fiel to write
file = open("tmp.txt","a+")

# write three lines
file.write("First line\n")
file.write("Second line\n")
file.write("Third line\n")

# the file pointer is not in at the beginning of the file 
file.seek(0)

# print the first line of the file
first_line = file.readline()
print("\n____________First Line____________")
print(first_line)

# close the file
#file.close()


### Stretch Goal ###
file = open("config-pfSense.home.arpa-20230309233846.xml","r+")


content = file.read()
content = content.replace("Vasco Lucas","Vasco Coelho de Melo Gouveia Lucas")

# the file pointer is pointing to the end of the file and this is not what we want
file.seek(0)

file.write(content)

# because the file is shorter, it is necessary to remove any leftover data from the end of the file
file.truncate()

file.close()


# content = subprocess.run(["cat","tmp.txt"],capture_output=True, text=True)
#print(content.stdout)

# removes the file
subprocess.run(["rm","tmp.txt"],capture_output=True, text=True)

### ---------------------------------------------------------------------- ###
################## it is necessary to import the file again ##################
### ---------------------------------------------------------------------- ###


