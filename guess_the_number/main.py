import tkinter as tk
import random

def check_guess():
    guess = int(entry.get())
    global attempts
    attempts += 1

    if guess < number:
        result_label.config(text="Too low!")
    elif guess > number:
        result_label.config(text="Too high!")
    else:
        result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts")

def reset_game():
    global number, attempts

    number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100")

root = tk.Tk()
root.title(f"Number Guessing Game")

number = random.randint(1, 100)
attempts = 0

prompt_label = tk.Label(root, text="Guess a number between 1 and 100")
prompt_label.pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack()

root.mainloop()