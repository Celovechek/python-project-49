#!/usr/bin/env python3
from random import randint


GAME_Q = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(NUMBER):
    if NUMBER == 0 or NUMBER == 1:
        return False
    DIVIDER = 2
    while NUMBER % DIVIDER != 0:
        DIVIDER += 1
    return NUMBER == DIVIDER


def game():
    NUMBER = randint(0, 100)
    CORRECT_ANSWER = "yes" if prime_check(NUMBER) else "no"
    QUESTION_LIST = [NUMBER]
    return CORRECT_ANSWER, QUESTION_LIST


GAME_LIST = [GAME_Q, game]
