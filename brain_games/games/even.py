#!/usr/bin/env python3
from random import randint


GAME_Q = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    NUMBER = randint(0, 1000000)
    CORRECT_ANSWER = 'no' if NUMBER % 2 else 'yes'
    QUESTION = f'Question: {NUMBER}'
    return CORRECT_ANSWER, QUESTION


GAME_LIST = [GAME_Q, game]
