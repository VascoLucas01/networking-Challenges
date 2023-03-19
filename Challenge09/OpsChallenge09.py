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


    
    

    



