#!/usr/bin/python3

#Script : OpsChallenge09.sh
#Purpose: Practice python skills
#Why    : Understand how to work with conditional statements

threshold_value = 10
input_value = ""
i = 0

while(not input_value.isnumeric()):
    if(i != 0):
        print("Incorrect input value! Try again:")
    input_value = input("_____________The threshold value is 10_____________\nEnter a different integer value: ")
    
    i = i + 1

if(input_value > threshold_value):
    print("É maior!")
elif(input_value < threshold_value):
    print("É menor!")
else:
    print("É igual!")
    
    

    



