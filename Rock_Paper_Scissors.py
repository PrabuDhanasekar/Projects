import random

def play():
    User = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    Computer = random.choice(['r','s','p'])
    print("User choice is: "f"{User}")
    print("Computer choice is: "f"{Computer}")
    if User.lower() == Computer:
        print("It\'s a tie")
    
    elif Game(User.lower(), Computer):
        return "You are Won"

    else:
        return 'Your are lost'

def Game(player,com):
    if (player == 'r' and com == 's') or (player == 's' and com == 'p') or (player == 'p' and com == 'r'):
        return True

print(play())