import time
import random

def type_print(message: str) -> None:
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()

type_print("Welcome to Henry's 🪨📄✂️ game!")

def get_user_choice():
    while True:
        type_print("Enter your choice (rock, paper, scissors): ")
        user_choice = input().lower()
        if user_choice in ['rock' or 'r', 'paper' or 'p', 'scissors' or 's']:
            return user_choice
        else:
            type_print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        type_print(f"You chose: {user_choice}")
        type_print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        type_print(result)

        type_print("Do you want to play again? (yes/no): ")
        play_again = input().lower()
        if play_again != 'yes':
            break

    type_print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
