"""
Coding Challenge 2, morse.py
"""
# Coding Challenge 3, hangman.py
# Name: Eseka Precious
# Student No: 2024170


# A Morse code encoder/decoder

import os

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"),
    ("..-.", "F"), ("--.", "G"), ("....", "H"), ("..", "I"), (".---", "J"),
    ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"), ("---", "O"),
    (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"),
    ("..-", "U"), ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"),
    ("--..", "Z"), (".-.-.-", "."), ("-----", "0"), (".----", "1"),
    ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"),
    ("-.--.", "("), ("-.--.-", ")"), (".-...", "&"), ("---...", ":"),
    ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"),
    ("..--..", "?"), ("-.-.--", "!")
)

MORSE_LIST = [i for i in MORSE_CODE]

MORSE_LIST.append((" ", " "))

def print_intro():
    """
    A Welcome Message
    """
    print('Welcome to Wolmorse')
    print('This program encodes and decodes Morse code.')
    print('-------------------------')

def encode(ask):
    """
    Encoding an input
    ask can either be a list or a string
    """
    dic_e = {}
    for val in MORSE_LIST:
        dic_e[val[1]] = val[0]
    if ask is None:
        prompt_e = input('What message would you like to encode: ')
        d_e = []
        for val in prompt_e:
            if val == '':
                pass
            else:
                d_e.append(val.upper())
        x_e = ''
        for val in d_e:
            dic_e_str = dic_e[val]
            x_e = x_e + dic_e_str+ " "
        print(x_e)
        
    else:
        list_e = []
        d_e = []
        for i in ask:
            for j in i:
                if j == '':
                    pass
                elif isinstance(j, int):
                    d_e.append(j)
                else:
                    d_e.append(j.upper())
            x_e = ''
            for val in d_e:
                dic_e_str = dic_e[val]
                x_e = x_e + dic_e_str+ " "
            list_e.append(x_e)
        if isinstance(ask, list):
            return list_e
        else:
            return list_e[-1]

def decode(ask):
    """
    decoding an input
    ask take's a string
    """
    dic_d = {}
    for val in MORSE_LIST:
        dic_d[val[0]] = val[1]
    if ask is None:
        prompt_d = input('What message would you like to decode: ')
        split_prompt_d = prompt_d.split(' ')
        q_list = []
        for val in split_prompt_d:
            if val == "":
                if  ' ' in q_list:
                    pass
                else:
                    q_list.append(' ')
            else:
                q_list.append(val)
        x_str = ''
        for val in q_list:
            dic_str = dic_d[val]
            x_str = x_str + dic_str
        print(x_str)
    else:
        split_prompt_d = ask.split(' ')
        q_list = []
        for val in split_prompt_d:
            if val == "":
                if  ' ' in q_list:
                    pass
                else:
                    q_list.append(' ')
            else:
                q_list.append(val)
        x_str = ''
        for val in q_list:
            dic_str = dic_d[val]
            x_str = x_str + dic_str
        print(x_str)

def encoding(quest):
    """
    For Encoding or Decoding
    quest takes in an input as string
    """
    if quest == 'e':
        encode(ask=None)
    elif quest == 'd':
        decode(ask=None)
    else:
        print('Invalid Mode')

def get_input():
    """
    Docs
    """
    bols = False
    while not bols:
        quest = input('Would you like to encode (e) or decode (d): ').lower()
        if quest in ['d', 'e']:
            encoding(quest)
            bols = True
        else:
            print('Invalid Mode')

# ---------- Challenge Functions (Optional) ----------

def process_lines(filename, operation):
    """
    This function: takes two parameters
    Filename: A file that contains message to eithe be encoded or decoded
    Operation: Mode of operation (encoding/decoding) of the file.
    """
    try:
        file = open(filename)
        text = file.read()
        file.close()
        text = text.split('\n')
    except IOError as err:
        print(f"Unable to open the file: , {err}")
    if operation == 'e':
        print(encode(ask=text))
    elif operation == 'd':
        print(decode(ask=text))
    else:
        print('The Wrong Operation was used')

def check_file_exists(filename):
    """
    This checks if a file is exists
    """
    file = filename
    if os.path.exists(filename):
        return file
    else:
        print('Invalid Filename')
        promp = input('Enter a filename: ')
        check_file_exists(promp)
        return ''

def write_lines(value):
    """
    Create a file name results.txt where data can be stored
    Value = list of strings
    """
    file = open('result.txt', 'w')
    for data in value:
        file.write(f"{data}\n")
    file.close()

def get_filename_input():
    """
    Get Filename Input
    """
    bols = False
    while not bols:
        quest = input('Would you like to encode (e) or decode (d): ').lower()
        if quest in ['d', 'e']:
            bols = True

        else:
            print('Invalid Mode')
    prompt = input('Would you like to read from a file (f) or the console (c)? ').lower()
    if prompt == 'f':
        promp = input('Enter a filename: ')
        check_file_exists(promp)
        print('Output written to results.txt')
        #print(f'{quest}, None, {file}')
    elif prompt == 'c':
        if quest == 'e':
            promp = input('What message would you like to encode: ')
            print(encode(ask=promp))
            #print(f'{quest}, {promp}, None')
        else:
            promp = input('What message would you like to decode: ')
            decode(ask=promp)
            #print(f'{quest}, {promp}, None')
    else:
        print('Invalid Input')

def play():
    """
    Play function to ask user if there would quit or still play
    """
    while True:
        user = input("Play Again? (Y/N) ").upper()
        if user == 'Y':
            main()
        else:
            print('Thanks for using the program, goodbye!')
            return ''
        break

def main():
    """
    MAIN DRIVER FUNCTION
    """
    print_intro()
    get_filename_input()
    play()


if __name__ == '__main__':
    main()
