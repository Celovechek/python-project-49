#!/usr/bin/env python3
from .logic import loop, congratulations, welcome_user
from brain_games.games.progression import game


def main():
    global NAME
    NAME = welcome_user()
    progression()


def progression():
    global NAME
    congratulations(NAME, loop(NAME,
                               'What number is missing in the progression?',
                               game))


if __name__ == '__main__':
    main()
