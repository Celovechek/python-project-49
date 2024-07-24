import prompt


def main():
    print('Welcome to the Brain Games!')


def welcome_user():
    global NAME
    print('Welcome to the Brain Games!')
    NAME = prompt.string("May I have your name? ")
    print(f"Hello, {NAME}!")
    return NAME


def play(NAME, GAME_Q, game):
    print(GAME_Q)
    ROUNDS = 3
    for i in range(ROUNDS):
        CORRECT_ANSWER, QUESTION_LIST = game()
        print(f'Question: {" ".join(map(str, QUESTION_LIST))}')
        USERS_ANSWER = input('Your answer: ')
        if CORRECT_ANSWER == USERS_ANSWER:
            print('Correct!')
        else:
            print(f"'{USERS_ANSWER}' is wrong answer ;(."
                  f"Correct answer was '{CORRECT_ANSWER}'.\n"
                  f"Let's try again, {NAME}!")
            return
    if i == ROUNDS - 1:
        print(f'Congratulations, {NAME}!')


if __name__ == '__main__':
    main()
