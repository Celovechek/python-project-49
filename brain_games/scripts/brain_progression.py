#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    progression()


def progression():
    global NAME
    congratulations(NAME, loop(NAME,
                               'What number is missing in the progression?',
                               'progression'))


if __name__ == '__main__':
    main()
