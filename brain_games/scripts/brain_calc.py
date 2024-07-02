#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    calc()


def calc():
    global NAME
    congratulations(NAME, loop(NAME,
                               'What is the result of the expression?',
                               'calc'))


if __name__ == '__main__':
    main()
