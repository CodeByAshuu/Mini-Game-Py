#--Tic Tac Toe Game for 2 Playerr--- 

import sys
#Made By : Sagar Sahu
# @Twitter : Ashuuu_7
# LinkedIn : www.linkedin.com/in/sagarr7
# Github   : https://github.com/CodeByAshuu


# Board
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

# Current Player = X
player = 'X'

# Displaying which player's turn is next
pseudoPlayer = "X"

# Places that have been filled
slotsFilled = 0


# Draw the Tic Tac Toe Board
def drawBoard():
    print("-------------")
    print("| " + board[0] + " | " + board[1] + ' | ' + board[2] + ' |')
    print("|-----------|")
    print("| " + board[3] + " | " + board[4] + ' | ' + board[5] + ' |')
    print("|-----------|")
    print("| " + board[6] + " | " + board[7] + ' | ' + board[8] + ' |')
    print("-------------")
    print(pseudoPlayer + "'s turn")


# Check if the game has been won or Tied
def checkGameWon():
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[7] == board[4] == board[1] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]) and (player == 'X' or player == 'O'):
        print("")
        print("**************")
        print("Game won by " + pseudoPlayer)
        print("🎉")
        print("**************")
        sys.exit()
    elif slotsFilled == 9:
        print("")
        print("**************")
        print("Game Tied")
        print("    -_-")
        print("**************")
        sys.exit()


# Function to take user input and update the board
def takeUserInput():
    global player
    global pseudoPlayer
    global slotsFilled

    position = input("Enter a position (0-8): ")

    # Check if the input is valid
    if not position.isdigit() or int(position) < 0 or int(position) > 8 or board[int(position)] == 'X' or board[
        int(position)] == 'O':
        print("Invalid input. Please enter a valid position.")
        return

    # Update the board
    board[int(position)] = player

    # Update slotsFilled
    slotsFilled += 1

    # Switch to the other player
    player = 'X' if player == 'O' else 'O'
    pseudoPlayer = 'X' if pseudoPlayer == 'O' else 'O'


# Main game loop
while True:
    drawBoard()
    takeUserInput()
    checkGameWon()

#Write code here
#Take input from the user and place it on the Board