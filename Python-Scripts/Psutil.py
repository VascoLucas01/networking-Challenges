#!/usr/bin/python3

import psutil
import subprocess

#Script : Psutil.py
#Purpose: Practice python skills
######### Time spent by normal processes executing in user mode
######### Time spent by processes executing in kernel mode
######### Time when system was idle
######### Time spent by priority processes executing in user mode
######### Time spent waiting for I/O to complete.
######### Time spent for servicing hardware interrupts
######### Time spent for servicing software interrupts
######### Time spent by other operating systems running in a virtualized environment
######### Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
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
    subprocess.run(f'echo "{i}" >> info.txt', shell=True)
    subprocess.run(f'echo "{cpu_times[j]}" >> info.txt', shell=True)
    subprocess.run(f'echo "" >> info.txt', shell=True)
    j += 1

subprocess.run(f'echo "> All in a tuple" >> info.txt', shell=True)
subprocess.run(f'echo "{cpu_times}" >> info.txt', shell=True)

### Stretch Goal ###
