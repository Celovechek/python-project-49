#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    even()


def even():
    global NAME
    print('Answer "yes" if the NUMBER is even, otherwise answer "no".')
    for i in range(3):
        NUMBER = randint(0, 1000000)
        CORRECT_ANSWER = 'no' if NUMBER % 2 else 'yes'
        if algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'QUESTION: {NUMBER}'):
            return
    congratulations(NAME, i)


if __NAME__ == '__main__':
    main()
