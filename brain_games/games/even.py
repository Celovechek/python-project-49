#!/usr/bin/env python3
from random import randint


GAME_Q = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_check(NUMBER):
    return not (bool(NUMBER % 2))


def game():
    NUMBER = randint(0, 1000000)
    CORRECT_ANSWER = 'yes' if even_check(NUMBER) else 'no'
    QUESTION = f'Question: {NUMBER}'
    return CORRECT_ANSWER, QUESTION


GAME_LIST = [GAME_Q, game]
