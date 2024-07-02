#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    prime()


def prime():
    global NAME
    congratulations(NAME, loop(NAME,
                               'Answer "yes" if given number is prime. '
                               'Otherwise answer "no".',
                               'prime'))


if __name__ == '__main__':
    main()
