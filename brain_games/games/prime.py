#!/usr/bin/env python3
from random import randint


GAME_Q = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_script(NUMBER):
    if NUMBER == 0 or NUMBER == 1:
        return "no"
    DIVIDER = 2
    while NUMBER % DIVIDER != 0:
        DIVIDER += 1
    return "yes" if NUMBER == DIVIDER else "no"


def game():
    NUMBER = randint(0, 100)
    CORRECT_ANSWER = prime_script(NUMBER)
    QUESTION = f'Question: {NUMBER}'
    return CORRECT_ANSWER, QUESTION


GAME_LIST = [GAME_Q, game]
