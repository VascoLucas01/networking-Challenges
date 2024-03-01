#!/usr/bin/python3

#Script : BashInPython.py
#Purpose: Run bash command with modules os and subprocess provided by python
######### The Python module “os” must be utilized
######### At least three variables must be declared in Python that contain results of bash operations
######### The Python function print() must be used at least three times
#Why    : Quick understand of the differences between python and bash script


import os
import subprocess


whoami_os = os.popen("whoami 2>/dev/null").read()
ip_a_os = os.popen("ip a 2>/dev/null").read()
lshw_short_os = os.popen("lshw -short 2>/dev/null").read()

print("______________________ With module OS ______________________")
print("----------> First command : whoami")
print(whoami_os)
print("----------> Second command : ip a")
print(ip_a_os)
print("----------> Third command : lshw -short")
print(lshw_short_os)



whoami_subprocess = subprocess.run(["whoami"],capture_output=True, text=True)
ip_a_subprocess = subprocess.run(["ip","a"],capture_output=True, text=True)
lshw_short_subprocess = subprocess.run(["lshw","-short"],capture_output=True, text=True)



print("______________________ With module SUBPROCESS ______________________")
print("----------> First command : whoami")
print(whoami_subprocess.stdout)
print("----------> Second command : ip a")
print(ip_a_subprocess.stdout)
print("----------> Third command : lshw -short")
print(lshw_short_subprocess.stdout)
