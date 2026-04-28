"""
Tic-Tac-Toe with AI Opponent
CMPSC 132 – Final Project Enhancement

Modes:
  Easy   – AI picks a random available square
  Medium – AI plays perfectly 50% of the time, randomly 50% of the time
  Hard   – AI plays perfectly every time using the Minimax algorithm
"""

import random

#  Board Utilities

def make_board():
    """Return a fresh 3×3 board filled with spaces."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    """Display the current board state with row/column guides."""
    print("\n    0   1   2")
    print("  +---+---+---+")
    for r, row in enumerate(board):
        print(f"{r} | {' | '.join(row)} |")
        print("  +---+---+---+")
    print()


def available_moves(board):
    """Return a list of (row, col) tuples for every empty cell."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']


def make_move(board, row, col, player):
    """Place player's mark on the board."""
    board[row][col] = player


def check_winner(board, player):
    """Return True if the given player has won."""
    # Rows and columns
    for i in range(3):
        if all(board[i][c] == player for c in range(3)):
            return True
        if all(board[r][i] == player for r in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    """Return True if the board is full and there is no winner."""
    return len(available_moves(board)) == 0


def game_over(board):
    """Return True if either player has won or the board is full."""
    return check_winner(board, 'X') or check_winner(board, 'O') or is_draw(board)

#  Minimax Algorithm  (used by Hard & Medium AI)

def minimax(board, is_maximizing):
    """
    Recursively evaluate every possible game state.

    The AI is always 'O' (maximizing player).
    The human is always 'X' (minimizing player).

    Returns an integer score:
       +1  → AI wins
       -1  → Human wins
        0  → Draw
    """
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    moves = available_moves(board)

    if is_maximizing:
        best = -2
        for (r, c) in moves:
            board[r][c] = 'O'
            score = minimax(board, False)
            board[r][c] = ' '
            best = max(best, score)
        return best
    else:
        best = 2
        for (r, c) in moves:
            board[r][c] = 'X'
            score = minimax(board, True)
            board[r][c] = ' '
            best = min(best, score)
        return best


def best_move(board):
    """Return the (row, col) that gives the AI the highest Minimax score."""
    best_score = -2
    move = None
    for (r, c) in available_moves(board):
        board[r][c] = 'O'
        score = minimax(board, False)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

#  AI Move Selection by Difficulty

def ai_move(board, difficulty):
    """
    Choose the AI's move based on difficulty level.

    Easy   – always random
    Medium – 50 % perfect (Minimax), 50 % random
    Hard   – always perfect (Minimax)
    """
    moves = available_moves(board)

    if difficulty == 'easy':
        return random.choice(moves)

    elif difficulty == 'medium':
        # Coin-flip: perfect or random
        if random.random() < 0.5:
            return best_move(board)
        else:
            return random.choice(moves)

    else:  # hard
        return best_move(board)

#  Human Input Handling

def get_human_move(board):
    """Prompt the human player for a valid row and column."""
    while True:
        try:
            row = int(input("  Enter row    (0-2): "))
            col = int(input("  Enter column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("  ✗ Coordinates must be between 0 and 2. Try again.\n")
            elif board[row][col] != ' ':
                print("  ✗ That cell is already taken. Try again.\n")
            else:
                return row, col
        except ValueError:
            print("  ✗ Please enter a number. Try again.\n")

#  Difficulty Menu

def choose_difficulty():
    """Ask the player to pick a difficulty and return the choice as a string."""
    print("  Select difficulty:")
    print("    1 – Easy   (AI plays randomly)")
    print("    2 – Medium (AI plays perfectly half the time)")
    print("    3 – Hard   (AI never makes a mistake)")
    while True:
        choice = input("  Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("  ✗ Invalid choice. Please enter 1, 2, or 3.\n")

#  Game Mode Menu

def choose_game_mode():
    """Ask whether to play against a human or the AI."""
    print("  Select game mode:")
    print("    1 – 2-Player (Human vs Human)")
    print("    2 – vs AI")
    while True:
        choice = input("  Enter 1 or 2: ").strip()
        if choice == '1':
            return 'two_player'
        elif choice == '2':
            return 'vs_ai'
        else:
            print("  ✗ Invalid choice. Please enter 1 or 2.\n")

#  Main Game Loop

def play_game():
    """Run a single game from start to finish."""
    print("\n" + "═" * 36)
    print("        TIC-TAC-TOE")
    print("═" * 36)

    mode = choose_game_mode()
    difficulty = None

    if mode == 'vs_ai':
        difficulty = choose_difficulty()
        print(f"\n  You are X. The AI ({difficulty.capitalize()} mode) is O.")
    else:
        print("\n  Player 1 is X. Player 2 is O.")

    board = make_board()
    # X always goes first
    current_player = 'X'

    while not game_over(board):
        print_board(board)

        if mode == 'vs_ai' and current_player == 'O':
            print("  AI is thinking…")
            row, col = ai_move(board, difficulty)
            print(f"  AI placed O at row {row}, column {col}.")
        else:
            player_label = "Player 1 (X)" if current_player == 'X' else "Player 2 (O)"
            if mode == 'vs_ai':
                player_label = f"Your turn (X)"
            print(f"  {player_label}'s move:")
            row, col = get_human_move(board)

        make_move(board, row, col, current_player)

        if check_winner(board, current_player):
            print_board(board)
            if mode == 'vs_ai':
                winner_msg = "You win! 🎉" if current_player == 'X' else "AI wins!"
            else:
                winner_msg = f"Player {'1' if current_player == 'X' else '2'} ({current_player}) wins! 🎉"
            print(f"  ★ {winner_msg}")
            return

        if is_draw(board):
            print_board(board)
            print("  It's a draw!")
            return

        # Swap turns
        current_player = 'O' if current_player == 'X' else 'X'


def main():
    """Entry point – runs the game and offers replay."""
    while True:
        play_game()
        print()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Thanks for playing!\n")
            break


if __name__ == "__main__":
    main()