from game_logic import get_computer_choice, determine_winner

def get_user_choice():
    """Prompt user for their choice"""
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")

def display_result(user_choice, computer_choice, winner):
    """Show game result"""
    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if winner == "tie":
        print("⚖️ It's a tie!")
    elif winner == "user":
        print("🎉 You win!")
    else:
        print("😢 Computer wins!")
