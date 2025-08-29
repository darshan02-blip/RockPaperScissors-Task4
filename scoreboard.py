class Scoreboard:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def update_score(self, winner):
        """Update scores based on winner"""
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_score(self):
        """Display current score"""
        return f"Scores -> You: {self.user_score} | Computer: {self.computer_score}"
