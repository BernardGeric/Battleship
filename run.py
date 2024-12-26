import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ships(board, ship_count):
    for _ in range(ship_count):
        while True:
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            if board[row][col] == ".":
                board[row][col] = "X"
                break

