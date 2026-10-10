import random
from words import WORDS
from feedback import evaluate

MAX_GUESSES = 6
SYMBOLS = {"green": "G", "yellow": "Y", "gray": "-"}


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def print_history(self):
        for n, (guess, fb) in enumerate(self.history, 1):
            marks = " ".join(SYMBOLS[f] for f in fb)
            print(f"{n}. {guess.upper()}   {marks}")

    def summary(self, outcome):
        print("\n---- summary ----")
        print("result:", outcome)
        print("word:", self.target.upper())
        print(f"guesses used: {len(self.history)}/{MAX_GUESSES}")
        self.print_history()

    def run(self):
        print(f"Wordle - {self.length} letters, {MAX_GUESSES} guesses. q to quit.")
        print("G = right spot, Y = wrong spot, - = not in word")
        outcome = "quit"
        while len(self.history) < MAX_GUESSES:
            guess = input("> ").strip().lower()
            if guess == "q":
                break
            if len(guess) != self.length or not guess.isalpha():
                print(f"enter a valid {self.length}-letter word.")
                continue
            self.history.append((guess, evaluate(self.target, guess)))
            print()
            self.print_history()
            print()
            if guess == self.target:
                outcome = "won"
                break
        else:
            outcome = "lost"
        self.summary(outcome)