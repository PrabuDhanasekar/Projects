# # Guess the Number Zero to Hundred
from random import *
ran = randint(0 ,100)

for number in range(1,6):   
    Guess = int(input(f"{number} Guess the Number 0 to 100: "))
    if(ran == Guess):
        print("Your Guess is correct")
    elif(ran < Guess):
        print("Your Guess is to high")
    elif(ran > Guess):
        print("Your Guess is to low")

print(f"Your all Guess are wrong the number is {ran}")