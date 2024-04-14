#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    prime_game()


def prime(NUMBER):
    if NUMBER == 0 or NUMBER == 1:
        return "no"
    DIVIDER = 2
    while NUMBER % DIVIDER != 0:
        DIVIDER += 1
    return "yes" if NUMBER == DIVIDER else "no"


def prime_game():
    global NAME
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        NUMBER = randint(0, 100)
        CORRECT_ANSWER = prime(NUMBER)
        if algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {NUMBER}'):
            return
    congratulations(NAME, i)


if __name__ == '__main__':
    main()
