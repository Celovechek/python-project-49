#!/usr/bin/env python3
from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def question_and_answer():
    start = 0
    end = 1000000
    number = randint(start, end)
    correct_answer = 'yes' if is_even(number) else 'no'
    question_list = [number]
    return correct_answer, question_list


GAME_LIST = (GAME_RULES, question_and_answer)
