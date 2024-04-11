import prompt
from random import randint


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
        print(f'Question: {number}')
        correct_answer = 'no' if number%2 else 'yes'
        users_answer = input('Your answer: ')
        if correct_answer == users_answer:
            print('Correct!')
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
