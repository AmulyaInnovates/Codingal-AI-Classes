import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Choices
choices = ['stone', 'paper', 'scissors']


def display_choices():
    print(Fore.CYAN + "\nChoose one:")
    print(Fore.YELLOW + "1. Stone")
    print("2. Paper")
    print("3. Scissors\n")


def get_player_choice():
    while True:
        display_choices()
        user_input = input(Fore.GREEN + "Enter your choice (1-3): " + Style.RESET_ALL)

        if user_input in ['1', '2', '3']:
            return choices[int(user_input) - 1]
        else:
            print(Fore.RED + "Invalid input! Please enter 1, 2, or 3.\n")


def get_computer_choice():
    return random.choice(choices)


def colored_choice(choice):
    if choice == 'stone':
        return Fore.WHITE + choice + Style.RESET_ALL
    elif choice == 'paper':
        return Fore.BLUE + choice + Style.RESET_ALL
    elif choice == 'scissors':
        return Fore.RED + choice + Style.RESET_ALL


def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == 'stone' and computer == 'scissors') or
        (player == 'paper' and computer == 'stone') or
        (player == 'scissors' and computer == 'paper')
    ):
        return "player"
    else:
        return "computer"


def display_result(player, computer, result, player_name):
    print("\n" + Fore.CYAN + "----- RESULT -----" + Style.RESET_ALL)
    print(f"{player_name} chose: {colored_choice(player)}")
    print(f"Computer chose: {colored_choice(computer)}\n")

    if result == "player":
        print(Fore.GREEN + f"{player_name} wins this round!\n")
    elif result == "computer":
        print(Fore.RED + "Computer wins this round!\n")
    else:
        print(Fore.YELLOW + "It's a tie!\n")


def play_game():
    print(Fore.MAGENTA + "Welcome to Stone-Paper-Scissors!\n")

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        result = decide_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result, player_name)

        # Score update
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        # Scoreboard
        print(Fore.CYAN + "Scoreboard:")
        print(f"{player_name}: {player_score} | Computer: {computer_score}\n")

        # Replay option
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(Fore.MAGENTA + "\nThanks for playing!")
            break


if __name__ == "__main__":
    play_game()
