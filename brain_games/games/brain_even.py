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
        if (
            (answer.lower() == 'yes' and random_number % 2 == 0)
            or (answer.lower() == 'no' and random_number % 2 != 0)
        ):
            print('Correct!')
            i += 1
        elif answer.lower() == 'yes' and random_number % 2 != 0:
            print(
                f"'yes' is wrong answer ;(. Correct answer was 'no'."
                f"\nLet's try again, {name}!"
            )
            break

        elif answer.lower() == 'no' and random_number % 2 == 0:
            print(
                f"'no' is wrong answer ;(. Correct answer was 'yes'. "
                f"\nLet's try again, {name}!"
            )
            break
        elif answer.lower() != 'yes' or 'no':
            print(f"it's wrong answer ;(. \nLet's try again, {name}!")
            break

    if i == 3:
        yuhoo()


if __name__ == '__main__':
    main()
