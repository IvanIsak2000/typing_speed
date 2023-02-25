import keyboard

import time
import os
import sys


def check_symbol(symbol):
    while True:

        if keyboard.read_key(symbol):
            break


def main(text):

    for symbol_index in range(len(text)):
        symbol = text[symbol_index]

        colored_symbol = f'\x1b[6;30;42m {symbol} \x1b[0m'
        print(colored_symbol)

        new_text = text.replace(text[:symbol_index], colored_symbol)
        print(new_text)
        check_symbol(symbol)

    os.system('cls')
    print('Completed!')
    z = input('Все ваши нажатия:\n')


if __name__ == '__main__':
    text = 'бублик вышел на улицу!'

    main(text)
