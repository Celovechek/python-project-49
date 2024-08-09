#!/usr/bin/env python3
from ..logic import play
from brain_games.games.prime import GAME_LIST


def main():
    prime()


def prime():
    play(*GAME_LIST)


if __name__ == '__main__':
    main()
