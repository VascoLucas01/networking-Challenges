#!/usr/bin/python3

import psutil
import subprocess

#Script : OpsChallenge11.py
#Purpose: Practice python skills
#Why    : Understand how to work with Psutil

info = ["> Time spent by normal processes executing in user mode",
        "> Time spent by priority processes executing in user mode",
        "> Time spent by processes executing in kernel mode",
        "> Time when system was idle",
        "> Time spent waiting for I/O to complete",
        "> Time spent for servicing hardware interrupts",
        "> Time spent for servicing software interrupts",
        "> Time spent by other operating systems running in a virtualized environment",
        "> Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel"]



subprocess.run(["touch","info.txt"])
subprocess.run(f'echo "" > info.txt', shell=True)

cpu_times = psutil.cpu_times()

j = 0;
for i in info:
    #print(i)
    #print(cpu_times[j])
    #print("")
    subprocess.run(f'echo "{i}" >> info.txt', shell=True)
    subprocess.run(f'echo "{cpu_times[j]}" >> info.txt', shell=True)
    subprocess.run(f'echo "" >> info.txt', shell=True)
    j += 1

subprocess.run(f'echo "> All in a tuple" >> info.txt', shell=True)
subprocess.run(f'echo "{cpu_times}" >> info.txt', shell=True)

exit(0)   
#print("> All in a tuple")
#print(cpu_times)

exit(0)
    
user      = cpu_times[0]
nice      = cpu_times[1]
system    = cpu_times[2]
idle      = cpu_times[3]
iowait    = cpu_times[4]
irq       = cpu_times[5]
softirq   = cpu_times[6]
steal     = cpu_times[7]
guest     = cpu_times[8]



print("\t> ",user)

print("\t> ",system)

print("\t> ",idle)

print("\t> ",nice)

print("\t> ",iowait)

print("\t> ",irq)

print("\t> ",softirq)

print("\t> ",steal)

print("\t> ",guest)

print(cpu_times)

### Stretch Goal ###
