#!/usr/bin/env python3


import random
from brain_games.scripts.welcome import greet
from brain_games.scripts.welcome import get_user_name
from brain_games.scripts.welcome import hello
from brain_games.scripts.welcome import create_randome_number
from brain_games.scripts.welcome import user_answer
from brain_games.scripts.welcome import yuhoo


start_num: int = create_randome_number()
step_num: int = create_randome_number()
count: int = 10


def create_progression(start_num, step_num, count):
    progression: list = []
    current = start_num
    for i in range(count):
        progression.append(current)
        current += step_num
    return progression


progression = []
progression_1 = []
correct_result = 0


def hide_sign(progression):
    index_missing_sign = random.randint(0, 9)
    correct_result = progression[index_missing_sign]
    progression_1: list = progression.copy()
    progression_1 = progression[:index_missing_sign] + ['..'] + \
        progression[index_missing_sign + 1:]
    return progression_1, correct_result


def main():
    greet()
    get_user_name()
    name = get_user_name()
    hello()
    print('What number is missing in the progression?')

    i = 0
    while i < 3:
        start_num: int = create_randome_number()
        step_num: int = create_randome_number()
        count: int = 10
        progression = create_progression(start_num, step_num, count)
        progression_1, correct_result = hide_sign(progression)
        print(f"Question: {progression_1}")
        answer = int(user_answer())

        if answer == correct_result:
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'."
                f"\nLet's try again, {name}!"
            )
            break

    if i == 3:
        yuhoo()


if __name__ == '__main__':
    main()
