#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nAnswer 'yes' if the number is even, otherwise answer 'no'.")

    i = 0
    while i < 3:
        random_number = randint(1, 1000)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if (
            (user_answer.lower() == 'yes' and random_number % 2 == 0) or
            (user_answer.lower() == 'no' and random_number % 2 != 0)
        ):
            print('Correct!')
            i += 1
        elif user_answer.lower() == 'yes' and random_number % 2 != 0:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
            break

        elif user_answer.lower() == 'no' and random_number % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {user_name}!")
            break
        elif user_answer.lower() != 'yes' or 'no':
            print(f"it's wrong answer ;(. \nLet's try again, {user_name}!")
            break

    if i == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
