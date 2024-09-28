import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x400")
        
        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 18))
        self.title_label.pack(pady=20)
        
        
        self.rock_button = tk.Button(root, text="Rock", width=15, command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(root, text="Paper", width=15, command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=5)
        
    
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)
        
        
        self.score_label = tk.Label(root, text="User: 0 | Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=20)
        
        
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        
        self.result_label.config(text=f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.\n{result}")
        
        
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")
        
        
        self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def reset_game(self):
        
        self.result_label.config(text="")
        

        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
