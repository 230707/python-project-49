#!/usr/bin/env python3

from random import randint
from brain_games.scripts.welcome import greet
from brain_games.scripts.welcome import get_user_name
from brain_games.scripts.welcome import hello
from brain_games.scripts.welcome import user_answer
from brain_games.scripts.welcome import yuhoo


def main():
    greet()
    get_user_name()
    name = get_user_name()  # определяем переменную name,
    # что бы далее ее просто использовать,
    # а не спрашивать у пользователя снова
    hello()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    i = 0
    while i < 3:
        random_number = randint(1, 1000)
        print(f'Question: {random_number}')
        answer = str(user_answer())
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer.lower() == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!"
            )
            break

    if i == 3:
        yuhoo()


if __name__ == '__main__':
    main()
