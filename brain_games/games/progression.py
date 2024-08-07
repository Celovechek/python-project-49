#!/usr/bin/env python3
from random import randint


GAME_Q = 'What number is missing in the progression?'


def game():
    START = randint(0, 100)
    STEP = randint(1, 100)
    LENGTH = randint(5, 15)
    PROGRESSION_LIST = []
    for _ in range(LENGTH):
        PROGRESSION_LIST.append(str(START))
        START += STEP
    CORRECT_ANSWER_POSITION = randint(0, LENGTH - 1)
    CORRECT_ANSWER = PROGRESSION_LIST[CORRECT_ANSWER_POSITION]
    PROGRESSION_LIST[CORRECT_ANSWER_POSITION] = '..'
    return CORRECT_ANSWER, PROGRESSION_LIST


GAME_LIST = [GAME_Q, game]
