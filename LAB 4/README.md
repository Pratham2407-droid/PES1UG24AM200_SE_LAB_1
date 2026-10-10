# Lab 4: VibeCoding

**Scenario 17: Wordle** &nbsp;|&nbsp; Python terminal game

| | |
|---|---|
| **Name** | Pratham S Reddy |
| **SRN** | PES1UG24AM200 |
| **Section** | D |
| **Working repo (commit history)** | [Pratham2407-droid/17_wordle](https://github.com/Pratham2407-droid/17_wordle) |
| **Original repo** | [SETAPESU26/17_wordle](https://github.com/SETAPESU26/17_wordle) |

---

## Overview

A terminal Wordle-style game. The starting code had broken duplicate-letter feedback and gaps in guess handling. I used an LLM as a coding assistant to reproduce the bug, fix it, and add the features listed in the scenario README, one task at a time with a separate commit for each.

## The original bug

`feedback.py` marked a letter yellow whenever it appeared anywhere in the target, without checking whether that copy was already used up.

With target `flame`, the guess `eeeee` showed four yellows and one green. The correct result is four grays and one green.

## Tasks and commits

| Task | Change | Commit |
|:---:|---|:---:|
| 1 | Fixed duplicate-letter feedback. Greens are resolved first, and each letter in the target can satisfy at most one letter in the guess. | `4decdd6` |
| 2 | Fixed guess handling. Invalid guesses no longer use a turn, max 6 accepted guesses, clean win and loss messages, `q` to quit. | `db9b021` |
| 3 | Added 4, 5 and 6 letter modes, extra words in `words.py`, and a length prompt at startup in `main.py`. | `57c9cb7` |
| 4 | Guess history after every accepted guess and a final session summary (result, word, guesses used). | `4eee8a2` |

## Project structure

```text
LAB 4/
├── README.md
├── requirements.txt
├── main.py
├── game.py
├── feedback.py
├── words.py
├── before.mp4
├── after.mp4
└── chat_history.pdf
```

| File | Purpose |
|---|---|
| `main.py` | Entry point, asks for word length |
| `game.py` | Game loop, guess history, summary |
| `feedback.py` | Letter evaluation rules |
| `words.py` | In-memory word list (4, 5 and 6 letters) |
| `requirements.txt` | No third-party packages needed |

## How to run

```bash
python main.py
```

Pick 4, 5 or 6 for the word length, then type guesses.

| Marker | Meaning |
|:---:|---|
| `G` | Right letter, right spot |
| `Y` | Right letter, wrong spot |
| `-` | Letter not in the word |

Type `q` at any time to quit and see the summary.

## Testing done

- [x] Repeated-letter guesses (`eeeee`, `aaaae`, `pppps`, `ffffff`)
- [x] Exact matches and all-gray guesses
- [x] Invalid length and non-letter input (turn count and history unchanged)
- [x] All three word lengths
- [x] Win on the final allowed guess
- [x] Loss after 6 wrong guesses
- [x] Quitting mid-game

## Deliverables

- [x] Before video (original buggy behaviour)
- [x] After video (fixes and all features working)
- [x] Updated code
- [x] Chat history PDF
- [x] Separate commit for each task
