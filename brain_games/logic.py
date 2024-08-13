import prompt

ROUNDS = 3


def play(game_rules, question_and_answer, rounds=ROUNDS):
    '''Structure of the games'''
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_rules)
    for i in range(rounds):
        correct_answer, question_list = question_and_answer()
        print(f'Question: {" ".join(map(str, question_list))}')
        users_answer = input('Your answer: ')
        if correct_answer == users_answer:
            print('Correct!')
        else:
            print(f"'{users_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    if i == rounds - 1:
        print(f'Congratulations, {name}!')
