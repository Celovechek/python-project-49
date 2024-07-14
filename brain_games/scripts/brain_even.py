#!/usr/bin/env python3
from .logic import play, welcome_user
from brain_games.games.even import GAME_LIST


def main():
    global NAME
    NAME = welcome_user()
    even()


def even():
    global NAME
    play(NAME, *GAME_LIST)


if __name__ == '__main__':
    main()
