'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''

import random

# List of words to choose from
words = ['apple', 'banana', 'orange', 'mango','guava','peach','kiwi','pear','cherry']

# Randomly choose a word from the list
word = random.choice(words)

# Create a list of underscores for the word's letters
word_display = ['_'] * len(word)

# Keep track of guesses
guesses = []

# Set the maximum number of guesses (Aur kitna guess krega bhai)
max_guesses = 6

# Function to check a guess huehue!
def check_guess(guess):
    # Update the word display with the guessed letter if it's correct
    for i in range(len(word)):
        if word[i] == guess:
            word_display[i] = guess
    
    # Add the guess to the list of guesses
    guesses.append(guess)
    
    # Check if the player has won
    if '_' not in word_display:
        print('Congratulations, you won!')
        print('The word was:', word)
        return True
    return False

# Main game loop
while True:
    # Display the word with underscores and any correct guesses
    print(' '.join(word_display))
    
    # Display the number of remaining guesses and the guesses so far
    print('Remaining guesses:', max_guesses - len(guesses))
    print('Guesses so far:', guesses)
    
    # Get the player's guess
    guess = input('Guess a letter: ')
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print('Invalid guess. Please enter a single letter.')
        continue
    
    # Check if the guess has already been made
    if guess in guesses:
        print('You already guessed that letter.')
        continue

    # Check if the guess is correct or not
    if guess in word:
        print('Correct!')
        if check_guess(guess):
            break
    else:
        print('Incorrect.')
        guesses.append(guess)
        if len(guesses) == max_guesses:
            print('Sorry, you lost. The word was:', word)
            break

#Write your Code here!
"""THANKS FOR PLAYING"""