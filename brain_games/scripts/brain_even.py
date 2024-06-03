#!/usr/bin/env python3

from brain_games.cli import welcome_user, get_user_name
import prompt
from random import randint


name = get_user_name()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

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
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
        elif user_answer.lower() == 'no' and random_number % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
