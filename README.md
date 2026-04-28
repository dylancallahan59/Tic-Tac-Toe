# Tic-Tac-Toe with AI Opponent
CMPSC 132 – Final Project | Spring 2026

A terminal-based Tic-Tac-Toe game written in Python. Play against a friend or challenge an AI opponent across three difficulty levels.

---

## Project Description

This project builds on the base Tic-Tac-Toe requirements by adding an AI opponent powered by the **Minimax algorithm**. Tic-Tac-Toe is a solved game, meaning two perfect players will always draw. The AI takes advantage of this by calculating the best possible move every turn on Hard mode.

**Three difficulty levels:**

| Mode   | Behavior |
|--------|----------|
| Easy   | AI picks a random open square every turn |
| Medium | AI plays perfectly 50% of the time, randomly the other 50% |
| Hard   | AI uses Minimax and never makes a mistake |

**Game modes:**
- 2-Player (Human vs Human)
- 1-Player (Human vs AI)

---

## How to Run

**Requirements:** Python 3 (no external libraries needed)

1. Clone the repository
   ```
   git clone https://github.com/YOUR_USERNAME/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Run the game
   ```
   python3 tic_tac_toe.py
   ```

3. Follow the on-screen prompts to choose a game mode and difficulty.

---

## How to Play

- The board is a 3x3 grid. Rows and columns are numbered 0 to 2.
- Player X always goes first.
- When it is your turn, enter a row number (0-2) and a column number (0-2).
- The game ends when someone gets three in a row (horizontally, vertically, or diagonally) or the board fills up with no winner.

**Example move:**
```
    0   1   2
  +---+---+---+
0 |   |   |   |
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 |   |   |   |
  +---+---+---+

  Enter row    (0-2): 1
  Enter column (0-2): 1
```

---

## File Structure

```
tic-tac-toe/
├── tic_tac_toe.py   # Main game file
└── README.md        # Project documentation
```

---

## Features

- 3x3 board displayed after every move
- Input validation (rejects letters, out-of-range numbers, and occupied cells)
- Win detection for rows, columns, and both diagonals
- Draw detection when the board is full
- Replay option at the end of each game
- AI difficulty selection (Easy, Medium, Hard)
