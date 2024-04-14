#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global name
    name = welcome_user()
    prime_game()


def prime(number):
    if number == 0 or number == 1:
        return "no"
    divider = 2
    while number % divider != 0:
        divider += 1
    return "yes" if number == divider else "no"


def prime_game():
    global name
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        number = randint(0, 100)
        correct_answer = prime(number)
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {number}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
