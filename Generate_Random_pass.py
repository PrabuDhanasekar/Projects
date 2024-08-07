# Project Random Password

import random
print("Welcome to password Generator")

char = "abcdefghijkmnopqrstuvwxyzZYXWVUTSRQPONMKJIHGFEDCBA!@#$%^&*();,./':0123456789"

number = input("Amount of password Generate: ")
number = int(number)

length = input("Input your password lenght: ")
length = int(length)

for pwd in range(number):
    password = ""
    for n in range(length):
        password += random.choice(char)
    print(f"Your Random Password {pwd+1} is : {password}")