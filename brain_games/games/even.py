#!/usr/bin/env python3
from random import randint
from brain_games.scripts.logic import algorithm


GAME_Q = 'Answer "yes" if the number is even, otherwise answer "no".'


def game(NAME):
    NUMBER = randint(0, 1000000)
    CORRECT_ANSWER = 'no' if NUMBER % 2 else 'yes'
    return algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {NUMBER}')


GAME_LIST = [GAME_Q, game]
