#!/usr/bin/env python3
from random import randint, choice
from .logic import algorithm, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    calc()


def calc():
    global NAME
    print('What is the result of the expression?')
    for i in range(3):
        FIRST_NUMBER = randint(0, 1000)
        SECOND_NUMBER = randint(0, 1000)
        OPERATION = choice([' + ', ' - ', ' * '])
        CORRECT_ANSWER = str(eval(str(FIRST_NUMBER) + OPERATION + str(SECOND_NUMBER)))
        if algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'QUESTION: {FIRST_NUMBER}{OPERATION}{SECOND_NUMBER}'):
            return
    congratulations(NAME, i)


if __name__ == '__main__':
    main()
