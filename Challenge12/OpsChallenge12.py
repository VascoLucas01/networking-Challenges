#!/usr/bin/python3

#Script : OpsChallenge12.py
#Purpose: Practice python skills
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

        