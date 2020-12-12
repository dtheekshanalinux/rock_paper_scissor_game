# import the random module to create the random numbers
# Hellow world
while(True):
    import random
    # gui for user interface
    print("you have three choices they are")
    print("rock paper scissors")
    # variables
    c_won = "computer won!"
    u_won = "Congratulation you won!"
    # assign computer choices
    computer = random.choice(["rock","paper","scissors"])
    # gets the user choice
    user = input("Enter your choice ").lower()
    # play the game
    if computer == user:
        print("Tie.")
    elif computer == "rock":
        if user == "scissors":
            print(c_won)
        else:
            print(u_won)
    elif computer == "paper":
        if user == "rock":
            print(c_won)
        else:
            print(u_won)
    elif computer == "scissors":
        if user == "paper":
            print(c_won)
        else:
            print(u_won)
    answer = input("enter your choice yes or no (y/n) ")
    if answer == "n":
        break