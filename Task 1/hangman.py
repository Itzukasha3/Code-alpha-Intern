import random
import tkinter as tk
from tkinter import messagebox
import time

# Word list
words = ['python', 'developer', 'hangman', 'programming', 'algorithm', 'beginner', 'learning', 'simple']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎩 Hangman Game 🎭")
        self.root.geometry("600x500")
        self.root.configure(bg="#34495e")
        
        self.word = random.choice(words)
        self.guessed_letters = set()
        self.correct_letters = set(self.word)
        self.attempts = 6

        self.word_display = tk.StringVar()
        self.update_display()

        self.label = tk.Label(root, textvariable=self.word_display, font=("Arial", 28, "bold"), fg="white", bg="#34495e")
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Arial", 18), justify='center', bg="#ecf0f1")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.guess_letter())  # Bind Enter key
        
        self.guess_button = tk.Button(root, text="🎯 Guess", command=self.guess_letter, font=("Arial", 16, "bold"), bg="#e74c3c", fg="white", relief="raised")
        self.guess_button.pack(pady=5)
        
        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts}", font=("Arial", 18), fg="white", bg="#34495e")
        self.attempts_label.pack(pady=10)

        self.hangman_canvas = tk.Canvas(root, width=250, height=250, bg="#34495e", highlightthickness=0)
        self.hangman_canvas.pack()
        self.draw_hangman()
    
    def update_display(self):
        display_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.word_display.set(display_word)
    
    def draw_hangman(self):
        self.hangman_canvas.delete("all")
        parts = [
            (100, 230, 100, 40),  # Pole
            (100, 40, 170, 40),    # Beam
            (170, 40, 170, 70),    # Rope
            (155, 70, 185, 100),   # Head
            (170, 100, 170, 160),  # Body
            (150, 120, 190, 120),  # Arms
            (160, 160, 180, 200)   # Legs
        ]
        for i in range(7 - self.attempts):
            self.hangman_canvas.create_line(parts[i], fill="white", width=4)
    
    def guess_letter(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("⚠ Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("🔁 Already Guessed", "You already guessed that letter!")
            return

        self.guessed_letters.add(guess)
        
        if guess in self.correct_letters:
            messagebox.showinfo("✅ Correct!", "Nice! You found a letter.")
        else:
            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            messagebox.showerror("❌ Wrong Guess", "Oops! That letter is not in the word.")
            self.draw_hangman()
        
        self.update_display()
        self.check_game_over()
    
    def check_game_over(self):
        if self.correct_letters == self.guessed_letters:
            messagebox.showinfo("🎉 You Win!", f"Congratulations! The word was '{self.word}'")
            time.sleep(1)
            self.root.quit()
        elif self.attempts == 0:
            messagebox.showerror("💀 Game Over", f"You lost! The word was '{self.word}'")
            time.sleep(1)
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
