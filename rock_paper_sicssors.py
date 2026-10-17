
import random
    
moves = ["rock", "paper", "scissors"]

def ai_move(player_history):
    if len(player_history) >= 3 and random.random() < 0.5:
        most_common = max(set(player_history),
                        key=player_history.count)

        if most_common == "rock":
            return "paper"
        elif most_common == "paper":
            return "scissors"
        else:
            return "rock"

    return random.choice(moves)

def find_winner(player, computer):
    if player == computer:
        return "draw"

    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        return "player"

    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    player_history = []

    print("================================")
    print("  ROCK, PAPER, SCISSORS GAME")
    print("================================")
    print("Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Type quit to stop the game.")

    while True:
        player = input("\nChoose rock, paper, or scissors: ")
        player = player.lower().strip()

        if player == "quit":
            break

        if player not in moves:
            print("Invalid choice! Please try again.")
            continue

        computer = ai_move(player_history)

        print("You chose:", player)
        print("Computer chose:", computer)

        result = find_winner(player, computer)

        if result == "player":
            print("You win this round!")
            player_score += 1

        elif result == "computer":
            print("The computer wins this round!")
            computer_score += 1

        else:
            print("It is a draw!")

        player_history.append(player)

        print("\nSCORE")
        print("You:", player_score)
        print("Computer:", computer_score)

        again = input("\nPlay another round? (yes/no): ")
        if again.lower().strip() != "yes":
            break

    print("\n========== FINAL SCORE ==========")
    print("Your score:", player_score)
    print("Computer score:", computer_score)

    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > player_score:
        print("The computer won the game!")
    else:
        print("The game ended in a draw!")

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()