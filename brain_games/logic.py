import prompt


def play(game_rules, question_and_answer, ROUNDS=3):
    '''Structure of the games'''
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_rules)
    for i in range(ROUNDS):
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
    if i == ROUNDS - 1:
        print(f'Congratulations, {name}!')
