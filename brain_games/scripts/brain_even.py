#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    even()


def even():
    global NAME
    congratulations(NAME, loop(NAME,
                               'Answer "yes" if the number is even, '
                               'otherwise answer "no".',
                               'even'))


if __name__ == '__main__':
    main()
