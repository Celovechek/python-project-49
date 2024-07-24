#!/usr/bin/env python3
from .logic import play
from brain_games.games.gcd import GAME_LIST


def main():
    gcd()


def gcd():
    play(*GAME_LIST)


if __name__ == '__main__':
    main()
