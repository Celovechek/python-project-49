import prompt
from random import randint, choice
from .logic import algorithm, congratulations


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    calc()


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def calc():
    global name
    print('What is the result of the expression?')
    for i in range(3):
        first_number = randint(0, 1000)
        second_number = randint(0, 1000)
        operation = choice([' + ', ' - ', ' * '])
        correct_answer = str(eval(str(first_number) + operation + str(second_number)))
        if algorithm(correct_answer,
                     name,
                     question=f'Question: {first_number}{operation}{second_number}'):
            return
    congratulations(name, i)


if __name__ == '__main__':
    main()
