#!/usr/bin/python3

#Script : OpsChallenge12.py
#Purpose: Practice python skills
#Why    : Understand how to work HTTP requests


methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]

input_URL    = input("Enter a URL: ")

print("Choose one of the methods: (number)")
i = 1
for method in methods:
    print(i,"- ",method)
    i = i+1

input_method = input("\n") 
match input_method:
    case "1":
        print("\n\n>1")
    case "2":
        print("\n\n>2")
    case "3":
        print("\n\n>3")
    case "4":
        print("\n\n>4")
    case "5":
        print("\n\n>5")
    case "6":
        print("\n\n>6")
    case "7":
        print("\n\n>7")

    