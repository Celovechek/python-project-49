#!/usr/bin/env python3
from random import randint, choice


GAME_Q = 'What is the result of the expression?'


def game():
    first_number = randint(0, 1000)
    second_number = randint(0, 1000)
    operation = choice(['+', '-', '*'])
    correct_answer = str(eval(str(first_number) + operation
                              + str(second_number)))
    question_list = [first_number, operation, second_number]
    return correct_answer, question_list


GAME_LIST = [GAME_Q, game]
