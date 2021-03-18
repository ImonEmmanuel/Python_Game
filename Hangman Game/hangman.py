"""
Coding Challenge 3, hangman.py
"""
# Coding Challenge 3, hangman.py
# Name: Eseka Precious
# Student No: 2024170

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import os
import random
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces

RESPONSES = [
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
    """
    Main
    """
    return random.choice(all_words)

def load_words():
    """
    Loading the words file
    """
    try:
        file = open(WORDLIST_FILENAME)
        text = file.read()
        file.close()
        wordlist = text.split(' ')
        print("Loading word list from file......")
        print(f"{len(wordlist)} words loaded")
        return wordlist
    except IOError as err:
        print(f"Unable to open the file: , {err}")

def is_word_guessed(word, letters_guessed):
    """
    a function that check if the word has been guessed
    correctly by the player
    """
    return len(set(word).intersection(set(letters_guessed))) == len(set(word))

def get_guessed_word(word, letter_guessed):
    """
    get the guessed word
    """
    word_completion = "_" * len(word)
    for letter in letter_guessed:
        if letter in word:
            index = [i for i, val in enumerate(word) if val == letter]
            word_list = list(word_completion)
            for ind in index:
                word_list[ind] = letter
            word_completion = "".join(word_list)
    return " ".join(word_completion)

def get_remaining_letters(letters_guessed):
    """
    get the remianing letters that has not been guessed by the player
    """
    val_str = ''
    rem = [val for val in ascii_lowercase if val not in letters_guessed]
    for i in rem:
        val_str = val_str + i
    return val_str

def hangman():
    """
    Main
    """
    print("Welcome to Hangman Ultimate Edition")
    #print(f"{RESPONSES[0]}".format(len(word)))
    #print("-------------")

def play():
    """
    Play function to ask user if there would quit or still play
    """
    while True:
        user = input("Play Again? (Y/N) ").upper()
        if user == 'Y':
            main()
        else:
            return ''


# ---------- Challenge Functions (Optional) ----------

def create_leaderboard():
    """
    if present or create a leaderboard template 
    """
    file = open('leaderboard.txt', 'w')
    space = ' '
    dash = '-'
    file.write(f"Score{space*13}Name")
    file.write(f'\n{dash*30}')
    file.close()

def leaderboard():
    """
    A function that returns the Leaderboard
    if present or create a leaderboard template 
    if none exists
    """
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt') as file:
            data = file.read()
            for val in data.split('\n'):
                print(val)
    else:
        create_leaderboard()

def get_score(name):
    """
    A function that returns the user score 
    if the name is found in the Leaderboard
    """
    with open('leaderboard.txt') as file:
        data = file.read()
    txt_list = []
    for val in data.split('\n'):
        txt_list.append(val)
    num = []
    names = []
    slice_file = txt_list[2:]
    for val in range(len(slice_file)):
        num.append(int(slice_file[val][:2]))
        names.append(slice_file[val][15:])
    try:
        dictx = {}
        for key, value in enumerate(names):
            dictx[value] = num[key]
        return dictx[name]
    except:
        update_score(names, 0)
        return 0

def save_score(name, score):
    """
    Save user score to the Leaderboard
    """
    with open('leaderboard.txt') as file:
        datax = file.read()
    if name in datax:
        txt_listx = []
        for val in datax.split('\n'):
            txt_listx.append(val)
        numx = []
        namesx = []
        slice_filex = txt_listx[2:]
        file_lengthx = len(slice_filex)
        for val in range(file_lengthx):
            numx.append(int(slice_filex[val][:2]))
            namesx.append(slice_filex[val][15:])
        if [numx[i] for i, val in enumerate(namesx) if val == name][0] < score and name in namesx:
            sck = input('A new personal best! Would you like to save your score(y/n): ')
            if sck == 'y':
                dictxx = {}
                for keyx, valuex in enumerate(namesx):
                    dictxx[valuex] = numx[keyx]
                dictxx[name] = score
                num_newx = [dictxx.get(i) for i in namesx]
                os.remove('leaderboard.txt')
                create_leaderboard()
                for i, val in enumerate(namesx):
                    if num_newx[i] > 0:
                        update_score(val, num_newx[i])
                    else:
                        pass
                print('Ok, your score has been saved')
            else:
                pass
        else:
            pass
    else:
        update_score(name, score)


def update_score(name, score):
    """
    Update the score if a person achieve a high score
    than his previous existing score on the leaderboard
    """
    file = open('leaderboard.txt', 'a') 
    space = " "
    if len(str(score)) == 1:
        file.write(f"\n{score}{space*13} {name}")
    elif len(str(score)) > 1:
        file.write(f"\n{score}{space*12} {name}")
    else:
        pass
    file.close()



# -----------------------------------

def main():
    """
    Main
    """
    wordlist = load_words()
    word = choose_random_word(wordlist)
    hangman()
    tries = 6
    # print(word)
    guessed_letter, guessed_word, word_complete = [], [], []
    guess = False

    while True:
        question = input('Do you want to Play (p) view the leaderboard (l) or quit (q): ').lower()
        try:
            if question in ['p', 'l', 'q']:
                if question == 'p':
                    name = input('Enter a name: ')
                    if os.path.exists('leaderboard.txt'):
                        get_score(name)
                    else:
                        create_leaderboard()
                    print(f"{RESPONSES[0]}".format(len(word)))
                    print("-------------")
            
                    while not guess and tries > 0:
                        print(f"You have {tries} guesses left")
                        print(f'{RESPONSES[5]}'.format(get_remaining_letters(guessed_letter)))
                        print("-------------")
                        letter_guessed = input('Please Enter a Letter: ').lower()
                        if len(letter_guessed) == 1 and letter_guessed.isalpha():
                            if letter_guessed in guessed_letter:
                                print(f"{RESPONSES[8]}".format(letter_guessed))
                                print("-------------")
                            elif letter_guessed not in word:
                                tries = tries - 1
                                print(f'{RESPONSES[4]}'.format(tries))
                                print(f'{RESPONSES[5]}'.format(get_remaining_letters(guessed_letter)))
                                if len(word_complete) == 0:
                                    print(f'{RESPONSES[7]}'.format("_ " * len(word)))
                                else:
                                    print(f'{RESPONSES[7]}'.format(word_complete[-1]))
                                print("-------------")
                                guessed_letter.append(letter_guessed)
                            else:
                                print(f'{RESPONSES[6]}'.format(letter_guessed))
                                guessed_letter.append(letter_guessed)
                                guessed_word.append(letter_guessed)
                                if len(guessed_word) == 1:
                                    print(get_guessed_word(word, letter_guessed))
                                    print("-------------")
                                    word_complete.append(get_guessed_word(word, letter_guessed))
                                else:
                                    word_split = word_complete[-1].split()
                                    ind = [i for i, val in enumerate(word) if val == letter_guessed]
                                    for i in ind:
                                        word_split[i] = letter_guessed
                                    print(" ".join(word_split))
                                    print("-------------")
                                    word_join = " ".join(word_split)
                                    word_complete.pop()
                                    word_complete.append(word_join)
                                    if '_' not in word_complete[-1].split():
                                        guess = is_word_guessed(word, guessed_letter)
                        elif letter_guessed not in ascii_lowercase:
                            tries = tries - 1
                            print(f'{RESPONSES[4]}'.format(tries))
                            print(f'{letter_guessed} is an Invalid Guess')
                    if guess:
                        print(f"{RESPONSES[1]}")
                        print(f'{RESPONSES[2]}'.format(tries * len(word)))
                        scores = tries * len(word)
                        save_score(name, score=scores)
                    else:
                        save_score(name, score=0)
                        print(f'{RESPONSES[3]}'.format(word))
                    play()

                elif question == 'l':
                    leaderboard()

        except Exception as err:
            print(err)
        finally:
            if question == 'q':
                print('Thanks for playing, goodbye!')
                return ''

# Driver function for the program
if __name__ == "__main__":
    main()
