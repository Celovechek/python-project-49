#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    gcd_game()


def gcd(FIRST_NUMBER, SECOND_NUMBER):
    while FIRST_NUMBER != SECOND_NUMBER:
        if FIRST_NUMBER > SECOND_NUMBER:
            FIRST_NUMBER -= SECOND_NUMBER
        else:
            SECOND_NUMBER -= FIRST_NUMBER
    return SECOND_NUMBER


def gcd_game():
    global NAME
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        FIRST_NUMBER = randint(0, 100)
        SECOND_NUMBER = randint(0, 100)
        CORRECT_ANSWER = str(gcd(FIRST_NUMBER, SECOND_NUMBER))
        if algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {FIRST_NUMBER} {SECOND_NUMBER}'):
            return
    congratulations(NAME, i)


if __name__ == '__main__':
    main()
