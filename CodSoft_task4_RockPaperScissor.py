import random
print("Welcome to the Rock - Paper - Scissor Game")

# Options for the game
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main game loop
while True:
    # User input
    user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop): ").lower()
    if user_choice == "quit":
        break
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Computer choice
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    result = determine_winner(user_choice, computer_choice)
    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    # Display scores
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Final scores
print("Game over!")
print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
print("Thanks for playing!")