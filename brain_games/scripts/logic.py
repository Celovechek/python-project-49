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


# flake8: noqa: C901
def loop(NAME, TASK, DISCIPLINE):
    if DISCIPLINE == 'even':
        from brain_games.games.even import game
    elif DISCIPLINE == 'calc':
        from brain_games.games.calc import game
    elif DISCIPLINE == 'gcd':
        from brain_games.games.gcd import game
    elif DISCIPLINE == 'progression':
        from brain_games.games.progression import game
    elif DISCIPLINE == 'prime':
        from brain_games.games.prime import game
    print(TASK)
    ROUNDS = 3
    for _ in range(ROUNDS):
        if game(NAME):
            break
    return _

def congratulations(NAME, i):
    if i == 2:
        print(f'Congratulations, {NAME}!')


if __name__ == '__main__':
    main()
