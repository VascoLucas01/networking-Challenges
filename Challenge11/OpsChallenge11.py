#!/usr/bin/python3

import psutil

#Script : OpsChallenge11.py
#Purpose: Practice python skills
#Why    : Understand how to work with Psutil

cpu_times = psutil.cpu_times()
user      = cpu_times[0]
system    = cpu_times[2]
idle      = cpu_times[3]
nice      = cpu_times[1]
iowait    = cpu_times[4]
irq       = cpu_times[5]
softirq   = cpu_times[6]
steal     = cpu_times[7]
guest     = cpu_times[8]


print("__________________Time spent by normal processes executing in user mode__________________")
print("\t> ",user)
print("__________________Time spent by processes executing in kernel mode__________________")
print("\t> ",system)
print("__________________Time when system was idle__________________")
print("\t> ",idle)
print("__________________Time spent by priority processes executing in user mode__________________")
print("\t> ",nice)
print("__________________Time spent waiting for I/O to complete__________________")
print("\t> ",iowait)
print("__________________Time spent for servicing hardware interrupts__________________")
print("\t> ",irq)
print("__________________Time spent for servicing software interrupts__________________")
print("\t> ",softirq)
print("__________________Time spent by other operating systems running in a virtualized environment__________________")
print("\t> ",steal)
print("__________________Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel__________________")
print("\t> ",guest)
print("__________________All in a tuple__________________")
print(cpu_times)

### Stretch Goal ###
# not done yet