#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user
from brain_games.games.prime import game


def main():
    global NAME
    NAME = welcome_user()
    prime()


def prime():
    global NAME
    congratulations(NAME, loop(NAME,
                               'Answer "yes" if given number is prime. '
                               'Otherwise answer "no".',
                               game))


if __name__ == '__main__':
    main()
