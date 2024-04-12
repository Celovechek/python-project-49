from random import randint
from .logic import algorithm, congratulations, welcome_user


def main():
    global name
    name = welcome_user()
    progression()


def progression():
    global name
    print('What number is missing in the progression?')
    for i in range(3):
        start = randint(0, 100)
        step = randint(1, 100)
        length = randint(5, 15)
        progression_list = []
        for _ in range(length):
            progression_list.append(str(start))
            start += step
        correct_answer_position = randint(0, length - 1)
        correct_answer = progression_list[correct_answer_position]
        progression_list[correct_answer_position] = '..'
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {" ".join(progression_list)}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
