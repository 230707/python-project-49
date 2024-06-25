#!/usr/bin/env python3


from brain_games.scripts.welcome import greet
from brain_games.scripts.welcome import get_user_name
from brain_games.scripts.welcome import hello
from brain_games.scripts.welcome import create_randome_number
from brain_games.scripts.welcome import user_answer
from brain_games.scripts.welcome import yuhoo

num = create_randome_number()
previous_num = 0


def check_prime(num):
    global previous_num
    while previous_num == num:
        num = create_randome_number()

    previous_num = num

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count


def main():
    greet()
    get_user_name()
    name = get_user_name()
    hello()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

    i = 0
    while i < 3:
        num = create_randome_number()
        count = check_prime(num)
        print(f'Question: {num}')
        answer = user_answer()

        if count == 2 or num == 1:
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
