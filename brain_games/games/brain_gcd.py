#!/usr/bin/env python3


from math import gcd
from brain_games.scripts.welcome import greet
from brain_games.scripts.welcome import get_user_name
from brain_games.scripts.welcome import hello
from brain_games.scripts.welcome import create_randome_number
from brain_games.scripts.welcome import user_answer
from brain_games.scripts.welcome import yuhoo


def main():
    greet()
    get_user_name()
    name = get_user_name()
    hello()
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:
        random_num_1 = create_randome_number()
        random_num_2 = create_randome_number()
        print(f"Question: {random_num_1} {random_num_2}")
        answer = int(user_answer())
        result = gcd(random_num_1, random_num_2)
        if answer == result:
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{result}'."
                f"\nLet's try again, {name}!"
            )
            break

    if i == 3:
        yuhoo()


if __name__ == '__main__':
    main()
