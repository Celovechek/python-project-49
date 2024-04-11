import prompt
from random import randint
from .logic import algorithm, congratulations


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    even()


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def even():
    global name
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(0, 1000000)
        correct_answer = 'no' if number % 2 else 'yes'
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {number}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
