#!/usr/bin/python3

#Script : Python_Requests_Library.py
#Purpose: Prompt the user to type a string input as the variable for your destination URL.
######### Prompt the user to select a HTTP Method of the following options:
############### GET
############### POST
############### PUT
############### DELETE
############### HEAD
############### PATCH
############### OPTIONS
######### Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
######### Using the requests library, perform a GET request against your lab web server.
######### For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
######### For the given URL, print response header information to the screen.
#Why    : Understand how to work HTTP requests

#######################IMPORTANT NOTE##############################
# URL format: https://www.example.com
###################################################################

import requests

methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]

# waits for URL
input_URL    = input("Enter a URL:\n>")


print("Choose one of the methods: (number)")
i = 1
for method in methods:
    print(i,"- ",method)
    i = i+1

# waits for HTTP method 
input_method = input("\n>") 
print("\n---------------------------------------")
print("URL         : ", input_URL)
print("HTTP method : ", methods[int(input_method)-1])
print("---------------------------------------")
confirmation = input("\n\nDo you want to proceed? (y/n)")
if(confirmation == "y"):   
    match input_method:
        case "1":
            response = requests.get(input_URL)
        case "2":
            response = requests.post(input_URL)
        case "3":
            response = requests.put(input_URL)
        case "4":
            response = requests.delete(input_URL)
        case "5":
            response = requests.head(input_URL)
        case "6":
            response = requests.patch(input_URL)
        case "7":
            response = requests.options(input_URL)
    
    print("\nResponse header: ", response.headers,"\n")
    
    if(response.status_code == 404):
        print("_____Site not found_____")
else:
    print("\nTerminating script...")
    exit(0)
    
    
#### Stretch goal not done yet ####
