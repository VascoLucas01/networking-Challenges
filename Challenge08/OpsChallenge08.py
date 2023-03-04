#!/usr/bin/python3

#Script : OpsChallenge08.sh
#Purpose: Practice python skills
#Why    : Understand how to work with list in pyhton

### variables
str = "aaa"
list = []

# fills the list with 10 positions
for i in range(0,10):
    list.insert(i,str)
 
# print the fourth element of the list
print(list[4])


# assuming [ position 0 .. position 9 ]
# print the last four elements
print(list[6:10])

# change the value of the seventh element to “onion”
list[6] = "onion"

print(list)



 


