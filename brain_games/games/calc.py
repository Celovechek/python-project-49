#!/usr/bin/env python3
from random import randint, choice


GAME_Q = 'What is the result of the expression?'


def game():
    FIRST_NUMBER = randint(0, 1000)
    SECOND_NUMBER = randint(0, 1000)
    OPERATION = choice([' + ', ' - ', ' * '])
    CORRECT_ANSWER = str(eval(str(FIRST_NUMBER) + OPERATION
                              + str(SECOND_NUMBER)))
    QUESTION = f'Question: {FIRST_NUMBER}{OPERATION}{SECOND_NUMBER}'
    return CORRECT_ANSWER, QUESTION


GAME_LIST = [GAME_Q, game]
