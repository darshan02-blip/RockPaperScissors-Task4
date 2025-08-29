import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Generate random choice for computer"""
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine winner based on game rules"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "scissors" and computer_choice == "paper") \
        or (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
