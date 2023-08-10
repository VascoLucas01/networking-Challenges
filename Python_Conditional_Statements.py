#!/usr/bin/python3

#Script : Python_Conditional_Statements.py
#Purpose: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
############### Equals: a == b
############### Not Equals: a != b
############### Less than: a < b
############### Less than or equal to: a <= b
############### Greater than: a > b
############### Greater than or equal to: a >= b
######### Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
######### Create an if statement that includes both elif and else to execute when both if and elif are not met.
#Why    : Understand how to work with conditional statements

threshold_value = 10
is_numeric = False
i = 0

while( not is_numeric ):

    input_value = input("\n_____________The threshold value is 10_____________\n\nEnter a different integer value: ")
    
    if( input_value.isnumeric() ):
        is_numeric = True
        break
    else:
        print("\n--- > Incorrect input value! < --- Try again:")
    

#if( int(input_value) > threshold_value ):
#    print("\n\t> It is higher than the threshold value!")
#elif( int(input_value) < threshold_value ):
#    print("\n\t> It is lower than the threshold value!")
#else:
#    print("\n\t> It is equal to the threshold value!")
    
    
### Stretch Goal ###
if( int(input_value) > threshold_value and int(input_value) < 20 ):
    print("\n\t> It is higher than the threshold value and lower than 20!")
# it is not efficient and does not make any sense, but it is just for demonstration
elif( int(input_value) < threshold_value or int(input_value) > 100):
    print("\n\t> It is lower than the threshold value or higher than 100!")
else:
    pass
