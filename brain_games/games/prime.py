#!/usr/bin/env python3
from random import randint
from brain_games.scripts.logic import algorithm


GAME_Q = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_script(NUMBER):
    if NUMBER == 0 or NUMBER == 1:
        return "no"
    DIVIDER = 2
    while NUMBER % DIVIDER != 0:
        DIVIDER += 1
    return "yes" if NUMBER == DIVIDER else "no"


def game(NAME):
    NUMBER = randint(0, 100)
    CORRECT_ANSWER = prime_script(NUMBER)
    return algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {NUMBER}')


GAME_LIST = [GAME_Q, game]
