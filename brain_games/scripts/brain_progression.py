#!/usr/bin/env python3
from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global NAME
    NAME = welcome_user()
    progression()


def progression():
    global NAME
    print('What number is missing in the progression?')
    for i in range(3):
        START = randint(0, 100)
        STEP = randint(1, 100)
        LENGTH = randint(5, 15)
        PROGRESSION_LIST = []
        for _ in range(LENGTH):
            PROGRESSION_LIST.append(str(START))
            START += STEP
        CORRECT_ANSWER_POSITION = randint(0, LENGTH - 1)
        CORRECT_ANSWER = PROGRESSION_LIST[CORRECT_ANSWER_POSITION]
        PROGRESSION_LIST[CORRECT_ANSWER_POSITION] = '..'
        if algorithm(CORRECT_ANSWER,
                     NAME,
                     QUESTION=f'Question: {" ".join(PROGRESSION_LIST)}'):
            return
    congratulations(NAME, i)


if __name__ == '__main__':
    main()
