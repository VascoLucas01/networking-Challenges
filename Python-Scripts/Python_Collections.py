#!/usr/bin/python3

#Script :  Python_Collections.py
#Purpose: Assign to a variable a list of ten string elements.
######### Print the fourth element of the list.
######### Print the sixth through tenth element of the list.
######### Change the value of the seventh element to “onion”.
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

### Creation of a tuple
# A tuple is an ordered, immutable collection of objects. 
# Tuples are similar to lists, but they cannot be modified once created.
tuple = (1,2,3)

### Creation of a set
# A set is an unordered collection of unique elements. 
# Sets are similar to lists or tuples, but they do not contain any duplicate elements.
set = {1,2,3,4,4,4}

# output = {1,2,3,4} -> because it is unordered
print(set)   

# remove the element 4
set.remove(4)

# output = {1,2,3}
print(set)

### Creation of a dictionary
# A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed.
dictionary = {"Cristiano" : "Ronaldo", "Sergio": "Ramos", "Diogo": "Costa"}

# print dictionary
print(dictionary)

# store the value associated with the name "Cristiano"
last_name_Cristiano = dictionary["Cristiano"]
print(last_name_Cristiano)
