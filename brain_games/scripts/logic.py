import prompt


def main():
    print('Welcome to the Brain Games!')


def welcome_user():
    global NAME
    print('Welcome to the Brain Games!')
    NAME = prompt.string("May I have your name? ")
    print(f"Hello, {NAME}!")
    return NAME


def algorithm(CORRECT_ANSWER, NAME, QUESTION):
    print(QUESTION)
    USERS_ANSWER = input('Your answer: ')
    if CORRECT_ANSWER == USERS_ANSWER:
        print('Correct!')
        return False
    else:
        print(f"'{USERS_ANSWER}' is wrong answer ;(."
              f"Correct answer was '{CORRECT_ANSWER}'.\n"
              f"Let's try again, {NAME}!")
        return True


def congratulations(NAME, i):
    if i == 2:
        print(f'Congratulations, {NAME}!')


if __name__ == '__main__':
    main()
