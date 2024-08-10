#!/usr/bin/env python3
from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return not (bool(number % 2))


def game():
    number = randint(0, 1000000)
    correct_answer = 'yes' if is_even(number) else 'no'
    question_list = [number]
    return correct_answer, question_list


GAME_LIST = [GAME_RULES, game]
