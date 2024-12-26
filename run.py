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

def is_valid_guess(guess, guesses):
    return 0 <= guess[0] < 6 and 0 <= guess[1] < 6 and guess not in guesses

def get_player_guess():
    while True:
        try:
            row = int(input("Guess a row (0-5): "))
            col = int(input("Guess a column (0-5): "))
            return (row, col)
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 5.")

def get_computer_guess(guesses):
    while True:
        guess = (random.randint(0, 5), random.randint(0, 5))
        if guess not in guesses:
            return guess

def play_battleship():
    # Get player's name
    player_name = input("Enter your name: ")


