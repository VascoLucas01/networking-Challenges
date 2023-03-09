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
file.close()



# content = subprocess.run(["cat","tmp.txt"],capture_output=True, text=True)
#print(content.stdout)

# removes the file
subprocess.run(["rm","tmp.txt"],capture_output=True, text=True)

