from game import WordleGame


def pick_length():
    while True:
        choice = input("word length (4/5/6): ").strip()
        if choice in ("4", "5", "6"):
            return int(choice)
        print("pick 4, 5 or 6.")


if __name__ == "__main__":
    WordleGame(pick_length()).run()