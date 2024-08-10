#!/usr/bin/env python3
from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 0 or number == 1:
        return False
    divider = 2
    while number % divider != 0:
        divider += 1
    return number == divider


def game():
    number = randint(0, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question_list = [number]
    return correct_answer, question_list


GAME_LIST = [GAME_RULES, game]
