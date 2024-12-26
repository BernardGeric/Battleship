Battleship Game

This is a simple implementation of the classic Battleship game where a player competes against the computer. The goal is to locate and "sink" all five ships hidden on the opponent's board before they sink yours.

Features

Turn-based gameplay: Players take turns guessing the locations of their opponent's ships.

Randomized ship placement: Ships are placed randomly on the board at the start of each game.

Input validation: Ensures guesses are within bounds and not repeated.

Scoring system: The first to sink all five ships wins the game.

How to Play

Run the game by executing the Python script.

Enter your name when prompted.

You will be shown your board with your ships placed.

Take turns guessing positions on the opponent's board.

Enter a row (0-5) and a column (0-5).

You will be informed if your guess is a hit or a miss.

The computer will also guess positions on your board.

The game ends when either you or the computer scores 5 hits.

Scores are displayed after each turn.

At the end, you will be notified of the winner.

Board Representation

.: Unoccupied cell

X: Ship position (hidden from the opponent)

H: Hit on a ship

M: Missed guess

Requirements

Python 3.x

Code Overview

Key Functions

print_board(board): Displays the current state of the board.

place_ships(board, ship_count): Randomly places the specified number of ships on the board.

is_valid_guess(guess, guesses): Validates a guess to ensure it is within bounds and hasn't been guessed before.

get_player_guess(): Prompts the player for a valid guess.

get_computer_guess(guesses): Generates a random valid guess for the computer.

play_battleship(): The main game loop, handling gameplay, turns, scoring, and the end condition.

Gameplay Flow

The player and computer boards are initialized as 6x6 grids filled with ..

Ships are placed randomly on both boards using place_ships().

The game alternates between the player's and computer's turns.

The game checks guesses against the opponent's board:

If a ship is hit, the cell is marked as H.

If missed, the cell is marked as M.

Scores are updated accordingly.

The game ends when one player scores 5 hits.
