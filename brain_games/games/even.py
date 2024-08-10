#!/usr/bin/env python3
from random import randint


GAME_Q = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_check(number):
    return not (bool(number % 2))


def game():
    number = randint(0, 1000000)
    correct_answer = 'yes' if even_check(number) else 'no'
    question_list = [number]
    return correct_answer, question_list


GAME_LIST = [GAME_Q, game]
