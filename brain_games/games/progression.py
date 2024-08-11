#!/usr/bin/env python3
from random import randint


GAME_RULES = 'What number is missing in the progression?'


def question_and_answer():
    start = randint(0, 100)
    step = randint(1, 100)
    length = randint(5, 15)
    progression_list = []
    for _ in range(length):
        progression_list.append(str(start))
        start += step
    correct_answer_position = randint(0, length - 1)
    correct_answer = progression_list[correct_answer_position]
    progression_list[correct_answer_position] = '..'
    return correct_answer, progression_list


GAME_LIST = [GAME_RULES, question_and_answer]
