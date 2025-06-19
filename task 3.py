import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    while True:
        user_input = input("\nYour move: ").lower()

        if user_input == "quit":
            print("\nThanks for playing!")
            break

        if user_input not in options:
            print("Invalid input. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif (
            (user_input == "rock" and computer_choice == "scissors") or
            (user_input == "paper" and computer_choice == "rock") or
            (user_input == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

        print(f"Score -> You: {user_wins} | Computer: {computer_wins}")

    print(f"\nFinal Score -> You: {user_wins} | Computer: {computer_wins}")

# Start the game
rock_paper_scissors()
