#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.logic import algorithm


GAME_Q = 'What is the result of the expression?'


def game(NAME):
    FIRST_NUMBER = randint(0, 1000)
    SECOND_NUMBER = randint(0, 1000)
    OPERATION = choice([' + ', ' - ', ' * '])
    CORRECT_ANSWER = str(eval(str(FIRST_NUMBER) + OPERATION
                              + str(SECOND_NUMBER)))
    return algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {FIRST_NUMBER}{OPERATION}'
                              f'{SECOND_NUMBER}')


GAME_LIST = [GAME_Q, game]
