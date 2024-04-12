import prompt


def main():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def algorithm(correct_answer, name, question):
    print(question)
    users_answer = input('Your answer: ')
    if correct_answer == users_answer:
        print('Correct!')
        return False
    else:
        print(f"'{users_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
        return True


def congratulations(name, i):
    if i == 2:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
