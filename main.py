import os
import sys
import random
from datetime import datetime
import string
import time

import readchar


def check_symbol_for_basic_mode(correct_key):

    print('\nWrong keystroke history: ')

    maschine_text = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits + string.punctuation

    for machine_key in random.choice(maschine_text):
        print(machine_key)

        if machine_key == correct_key:
            break
            time.sleep(0.1)


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
    print(f'Machine started in {started_time}')
    print(f'Machine finished in {finished_time}')
    print(f'Time: {int(finished_time[0:2]) - int(started_time[0:2])} hour {int(finished_time[3:5]) - int(started_time[3:5])} minutes {int(finished_time[6:8]) - int(started_time[6:8])} seconds')

    for_exit = input('Enter any button to exit...')


if __name__ == '__main__':
    mode = input(' Machine write mode(2)')

    if mode == '2':
        with open('texts.txt', 'r', encoding='utf-8') as text_file:
            texts = text_file.read()
            texts = texts.replace('\n', '').split('/')

            random_text = random.choice(texts)

        basic_mode(random_text)
