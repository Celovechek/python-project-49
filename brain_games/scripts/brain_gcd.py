#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    gcd()


def gcd():
    global NAME
    congratulations(NAME, loop(NAME,
                               'Find the greatest common divisor '
                               'of given numbers.',
                               'gcd'))


if __name__ == '__main__':
    main()
