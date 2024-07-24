#!/usr/bin/env python3
from random import randint


GAME_Q = 'Find the greatest common divisor of given numbers.'


def gcd_script(FIRST_NUMBER, SECOND_NUMBER):
    while FIRST_NUMBER != SECOND_NUMBER:
        if FIRST_NUMBER > SECOND_NUMBER:
            FIRST_NUMBER -= SECOND_NUMBER
        else:
            SECOND_NUMBER -= FIRST_NUMBER
    return SECOND_NUMBER


def game():
    FIRST_NUMBER = randint(0, 50)
    SECOND_NUMBER = randint(0, 50)
    CORRECT_ANSWER = str(gcd_script(FIRST_NUMBER, SECOND_NUMBER))
    QUESTION = f'Question: {FIRST_NUMBER} {SECOND_NUMBER}'
    return CORRECT_ANSWER, QUESTION


GAME_LIST = [GAME_Q, game]
