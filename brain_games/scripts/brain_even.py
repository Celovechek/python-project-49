#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global name
    name = welcome_user()
    even()


def even():
    global name
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(0, 1000000)
        correct_answer = 'no' if number % 2 else 'yes'
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {number}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
