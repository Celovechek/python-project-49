#!/usr/bin/env python3
from random import randint, choice

GAME_RULES = 'What is the result of the expression?'


def question_and_answer():
    '''Return correct answer and question list for calc game'''
    start = 0
    end = 1000
    first_number = randint(start, end)
    second_number = randint(start, end)
    operation = choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = str(first_number + second_number)
    elif operation == '-':
        correct_answer = str(first_number - second_number)
    elif operation == '*':
        correct_answer = str(first_number * second_number)

    question_list = [first_number, operation, second_number]
    return correct_answer, question_list


GAME_LIST = (GAME_RULES, question_and_answer)
