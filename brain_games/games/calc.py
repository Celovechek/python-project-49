#!/usr/bin/env python3
from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def question_and_answer():
    start = 0
    end = 1000
    first_number = randint(start, end)
    second_number = randint(start, end)
    operation = choice(['+', '-', '*'])
    correct_answer = str(eval(str(first_number) + operation
                              + str(second_number)))
    question_list = [first_number, operation, second_number]
    return correct_answer, question_list


GAME_LIST = [GAME_RULES, question_and_answer]
