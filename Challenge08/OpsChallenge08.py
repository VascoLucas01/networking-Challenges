#!/usr/bin/python3

#Script : OpsChallenge08.sh
#Purpose: Practice python skills
#Why    : Understand how to work with list in pyhton

### variables
str = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
list = []

# fill the list with 10 positions
print("__________fill the list one by one__________")
for i in range(0,10):
    list.insert(i,str[i])
    print(list)
 
# print the fourth element of the list
print("\nThe fourth element of the list: ")
print("> ", list[3])


# assuming [ position 0 .. position 9 ]
# print the last four elements
print("\nThe last five elements of the list:")
print("> ", list[5:10])

# change the value of the seventh element to “onion”
print("\nChange the value of the seventh element to \"onion\":")
list[6] = "onion"

print("> ", list)

################################# Stretch Goals not done yet #################################

 


