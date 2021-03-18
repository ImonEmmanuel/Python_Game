# Coding Challenge 3, hangman.py
# Name:
# Student No:

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    return random.choice(all_words)


# end of helper code
# -----------------------------------


def load_words():
    # TODO: Fill in your code here
    pass

# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function

# wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    # TODO: Fill in your the code here
    pass

def get_guessed_word(word, letters_guessed):
    # TODO: Fill in your code here
    pass

def get_remaining_letters(letters_guessed):
    # TODO: Fill in your code here
    pass

def hangman(word):
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("-------------")
    # TODO: Fill in your code here


# ---------- Challenge Functions (Optional) ----------

def get_score(name):
    pass

def save_score(name, score):
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

def main():
    # Uncomment the line below once you have finished testing.
    # word = choose_random_word(wordlist)

    # Uncomment the line below once you have implemented the hangman function.
    # hangman(word)
    pass

# Driver function for the program
if __name__ == "__main__":
    main()
