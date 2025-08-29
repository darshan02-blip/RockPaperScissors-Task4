from ui import get_user_choice, display_result
from game_logic import get_computer_choice, determine_winner
from scoreboard import Scoreboard

def main():
    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    scoreboard = Scoreboard()

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)
        scoreboard.update_score(winner)
        print(scoreboard.display_score())

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Final", scoreboard.display_score())
            break

if __name__ == "__main__":
    main()
