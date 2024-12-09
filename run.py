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

    # Initialize boards
    player_board = [["." for _ in range(6)] for _ in range(6)]
    computer_board = [["." for _ in range(6)] for _ in range(6)]

    # Place ships (5 each)
    place_ships(player_board, 5)
    place_ships(computer_board, 5)

    player_guesses = set()
    computer_guesses = set()
    player_score, computer_score = 0, 0

    print(f"Welcome to Battleship, {player_name}! Here is your board:")
    print_board(player_board)

    while player_score < 5 and computer_score < 5:
        print(f"\n{player_name}'s turn:")
        while True:
            player_guess = get_player_guess()
            if is_valid_guess(player_guess, player_guesses):
                player_guesses.add(player_guess)
                break
            else:
                print("Invalid guess. Try again.")

        if computer_board[player_guess[0]][player_guess[1]] == "X":
            print("You got a hit!")
            player_score += 1
        else:
            print("You missed.")

        print("\nComputer's turn:")
        computer_guess = get_computer_guess(computer_guesses)
        computer_guesses.add(computer_guess)
        print(f"Computer guessed: {computer_guess}")

        if player_board[computer_guess[0]][computer_guess[1]] == "X":
            print("Computer got a hit!")
            computer_score += 1
        else:
            print("Computer missed.")

        print("\nScores:")
        print(f"{player_name}: {player_score} | Computer: {computer_score}")

    if player_score == 5:
        print(f"Congratulations, {player_name}! You win!")
    else:
        print(f"The computer wins. Better luck next time, {player_name}!")

if __name__ == "__main__":
    play_battleship()
