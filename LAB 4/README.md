\# Lab 4: VibeCoding (Scenario 17, Wordle)



Name: Pratham S Reddy

SRN: PES1UG24AM200

Section: D



Code and commit history: https://github.com/Pratham2407-droid/17\_wordle

Original repo: https://github.com/SETAPESU26/17\_wordle



\## What this is



A terminal Wordle game in Python. The starting code had broken duplicate-letter feedback and a few gaps in guess handling, so I used an LLM as a coding assistant to fix those and add the features from the scenario README. The full chat history is in the PDF in this folder.



\## What I changed (one commit per task)



| Task | What | Commit |

|------|------|--------|

| 1 | Fixed duplicate-letter feedback. Greens are resolved first, and each letter in the target can only satisfy one letter in the guess. | 4decdd6 |

| 2 | Fixed guess handling. Invalid guesses no longer use up a turn, max 6 accepted guesses, clean win and loss messages, q to quit. | db9b021 |

| 3 | Added 4, 5 and 6 letter modes, extra words in words.py, length prompt at startup in main.py. | 57c9cb7 |

| 4 | Guess history printed after every accepted guess, plus a final summary (result, word, guesses used). | 4eee8a2 |



\## The original bug



`feedback.py` marked a letter yellow whenever it appeared anywhere in the target, without checking if that copy was already used. So with target `flame`, the guess `eeeee` showed four yellows and one green instead of four grays and one green.



\## Files



\- `main.py`: entry point, asks for word length

\- `game.py`: game loop, history and summary

\- `feedback.py`: letter evaluation rules

\- `words.py`: in-memory word list (4, 5 and 6 letter words)

\- `requirements.txt`: no third-party packages needed



\## How to run



Pick 4, 5 or 6 for the word length, then type guesses. G means right spot, Y means wrong spot, - means not in the word. Type q to quit.



\## Testing done



\- Repeated-letter guesses (eeeee, aaaae, pppps, ffffff)

\- Exact matches and all-gray guesses

\- Invalid length and non-letter input (turn count stays the same, nothing added to history)

\- All three word lengths

\- Win on the final allowed guess, loss after 6 wrong guesses, quitting mid-game



\## Deliverables in this folder



\- Before video (original buggy behaviour)

\- After video (all fixes and features working)

\- Updated code (the .py files above)

\- Chat history PDF

