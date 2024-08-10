#!/usr/bin/env python3
from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return second_number


def game():
    first_number = randint(0, 50)
    second_number = randint(0, 50)
    correct_answer = str(calculate_gcd(first_number, second_number))
    question_list = [first_number, second_number]
    return correct_answer, question_list


GAME_LIST = [GAME_RULES, game]
