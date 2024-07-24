#!/usr/bin/env python3
from .logic import play
from brain_games.games.even import GAME_LIST


def main():
    even()


def even():
    play(*GAME_LIST)


if __name__ == '__main__':
    main()
