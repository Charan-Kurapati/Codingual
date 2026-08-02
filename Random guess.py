# import random

# play=True

# num1=random.randint(0,9)

# print("I will generate a number from 0 to 9 and you will have to guess a number,1 digit at a time.")
# print("The game ends when you get 1 right guess")

# while play:
#     guess=int(input("Give me your best guess:"))
#     if num1==guess:
#         print("You won the game! the number was:",guess)
#         break

#     else:
#         print("Your guess isn't quite right guess again.")

#Rock paper scissors

import random

while True:
    user_action=input("Enter a choice(rock, paper, scissors): ")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print("f\nYou chose{user_action},computer chose{computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again=(input("Play again? (y/n): "))
    if play_again != "y":
        break