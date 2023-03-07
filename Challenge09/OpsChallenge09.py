#!/usr/bin/python3

#Script : OpsChallenge09.sh
#Purpose: Practice python skills
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
    


if( int(input_value) > threshold_value ):
    print("\n\t> É maior!")
elif( int(input_value) < threshold_value ):
    print("\n\t> É menor!")
else:
    print("\n\t> É igual!")
    
    

    



