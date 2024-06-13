import random
import time 

# Define symbol sets for different themes
symbols_default = ['🍒', '🍉', '🍋', '🔔', '🌟']
symbols_halloween = ['🎃', '👻', '💀', '🦇', '🍬']
symbols_christmas = ['🎄', '🎅', '🎁', '🛷', '⛄️']

def type_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print("")
def spin_row(symbols):
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    type_print("**************")
    type_print(" | ".join(row))
    type_print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] in ['🍒', '🎃', '🎄']:
            return bet * 3
        elif row[0] in ['🍉', '👻', '🎅']:
            return bet * 4
        elif row[0] in ['🍋', '💀', '🎁']:
            return bet * 5
        elif row[0] in ['🔔', '🦇', '🛷']:
            return bet * 10
        elif row[0] in ['🌟', '🍬', '⛄️']:
            return bet * 20
    return 0

def main():
    balance = 100

    type_print("*************************")
    type_print("Welcome to Python Slots")

    # Keep asking the user to choose a valid theme
    while True:
        type_print("Choose your theme (default(d) 🍒, halloween(h) 🎃, christmas(c) 🎄): ")
        theme = input().lower()
        if theme == "d":
            symbols = symbols_default
            type_print("Symbols: 🍒 , 🍉 , 🍋 , 🔔 , 🌟")
            break
        elif theme == "h":
            symbols = symbols_halloween
            type_print("Symbols: 🎃 , 👻 , 💀 , 🦇 , 🍬")
            break
        elif theme == "c":
            symbols = symbols_christmas
            type_print("Symbols: 🎄 , 🎅 , 🎁 , 🛷 , ⛄️")
            break
        else:
            type_print("Invalid theme choice. Please choose again.")

    type_print("*************************")

    while balance > 0:
        type_print(f"Current balance: ${balance}")

        type_print("Place your bet amount: ")
        bet = input()

        if not bet.isdigit():
            type_print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            type_print("Insufficient funds")
            continue

        if bet <= 0:
            type_print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row(symbols)
        type_print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            type_print(f"You won ${payout}")
        else:
            type_print("Sorry, you lost this round")

        balance += payout

        while True:
            type_print("Do you want to spin again? (Y/N): ")
            play_again = input().upper()
            if play_again not in ['Y', 'N']:
                type_print("Invalid input. Please enter 'Y' or 'N'.")
            else:
                break

        if play_again == 'N':
            break

    type_print("*******************************************")
    type_print(f"Game over! Your final balance is ${balance}")
    type_print("*******************************************")
    type_print("99% who are gamblers give up before winning big💰. Try again never give up 💪🏻")

if __name__ == '__main__':
    main()

