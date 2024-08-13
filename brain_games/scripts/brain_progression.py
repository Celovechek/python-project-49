#!/usr/bin/env python3
from ..logic import play
from brain_games.games.progression import GAME_LIST


def main():
    play(*GAME_LIST)


if __name__ == '__main__':
    main()
