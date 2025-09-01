#!/usr/bin/python3
"""
Simple Tic-Tac-Toe game for two players.
"""

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
        board (list): 2D list representing the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner.

    Args:
        board (list): 2D list representing the board.

    Returns:
        str: "X" or "O" if a player has won, or None if no winner yet.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    """
    Main function to play Tic-Tac-Toe between two players.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0
    winner = None

    while moves < 9 and winner is None:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter a number 0, 1, or 2.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        moves += 1
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()