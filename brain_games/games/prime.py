#!/usr/bin/env python3
from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    '''Return True if number is prime, else return False'''
    if number == 0 or number == 1:
        return False
    divider = 2
    while number % divider != 0:
        divider += 1
    return number == divider


def question_and_answer():
    '''Return correct answer and question list for prime game'''
    start = 0
    end = 100
    number = randint(start, end)
    correct_answer = "yes" if is_prime(number) else "no"
    question_list = [number]
    return correct_answer, question_list


GAME_LIST = (GAME_RULES, question_and_answer)
