#!/usr/bin/env python3
from random import randint
from brain_games.scripts.logic import algorithm


def gcd_script(FIRST_NUMBER, SECOND_NUMBER):
    while FIRST_NUMBER != SECOND_NUMBER:
        if FIRST_NUMBER > SECOND_NUMBER:
            FIRST_NUMBER -= SECOND_NUMBER
        else:
            SECOND_NUMBER -= FIRST_NUMBER
    return SECOND_NUMBER


def game(NAME):
    FIRST_NUMBER = randint(0, 100)
    SECOND_NUMBER = randint(0, 100)
    CORRECT_ANSWER = str(gcd_script(FIRST_NUMBER, SECOND_NUMBER))
    return algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {FIRST_NUMBER} {SECOND_NUMBER}')
