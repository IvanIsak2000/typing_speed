import os
import sys
import random
from datetime import datetime

import readchar


def keyboard_check():
    example_text = 'MIllerwa-s12345678910a,kind!and"compassionateman.'

    while True:
        for symbol in range(len(example_text)):
            random_symbol = random.choice(example_text)
            print(
                f'Random symbol is "{random_symbol}".To check the keypad readings, simply press this letter')

            user_key = readchar.readkey()

            if user_key == random_symbol:
                os.system('cls')
                print('Right!')

            else:
                os.system('cls')
                print('Wrong!')


def check_symbol_for_basic_mode(correct_key):
    
    print('\nWrong keystroke history: ')

    while True:

        user_key = readchar.readkey()
        print(user_key)

        if user_key == correct_key:
            break


def basic_mode(random_text):

    text = random_text

    started_time = datetime.now().strftime('%H:%M:%S')

    for symbol_index in range(len(text)):
        os.system('cls')
        correct_key = text[symbol_index]

        colored_symbol = f'\x1b[6;30;42m{correct_key}\x1b[0m'

        new_text = text.replace(text[:symbol_index + 1], colored_symbol)
        print(new_text)

        check_symbol_for_basic_mode(correct_key)

    finished_time = datetime.now().strftime('%H:%M:%S')

    os.system('cls')
    print('Completed!')
    print(f'You started in {started_time}')
    print(f'You finished in {finished_time}')

    for_exit = input('Enter any button to exit...')


if __name__ == '__main__':
    mode = input('Select Mode: Keyboard check(1) or Basic mode(2)')
    if mode == '1':
        keyboard_check()

    elif mode == '2':
        with open('texts.txt', 'r', encoding='utf-8') as text_file:
            texts = text_file.read()
            texts = texts.replace('\n', '').split('/')

            random_text = random.choice(texts)

        basic_mode(random_text)
