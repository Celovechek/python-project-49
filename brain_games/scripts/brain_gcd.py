#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global name
    name = welcome_user()
    gcd_game()


def gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return second_number


def gcd_game():
    global name
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        correct_answer = str(gcd(first_number, second_number))
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {first_number} {second_number}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
