
import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

print("================================")
print("       WELCOME TO HANGMAN       ")
print("================================")

# Main game loop
while wrong_guesses < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Take input from the player
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Display final result
else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
