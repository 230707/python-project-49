#!/usr/bin/env python3


# прописываем все необходимые нам импорты:
import random


from brain_games.scripts.welcome import greet
from brain_games.scripts.welcome import get_user_name
from brain_games.scripts.welcome import hello
from brain_games.scripts.welcome import create_randome_number
from brain_games.scripts.welcome import user_answer
from brain_games.scripts.welcome import yuhoo


# создаем функцию, которая будет рандомно генерить число1,
# число 2 и математический знак (+/-/*)
# чтобы математический знак не повторялся, вводим глобальную переменную,
# в коорую будем помещать результат предыдущего выбора:
previous_sign = None


def generate_random_math_operation():
    global previous_sign
    random_num_1 = create_randome_number()
    random_num_2 = create_randome_number()
    signs = ['+', '-', '*']
    chosen_sign = random.choice(signs)

    while previous_sign == chosen_sign:
        chosen_sign = random.choice(signs)

    previous_sign = chosen_sign

    return random_num_1, chosen_sign, random_num_2


# создаем функцию, которая получает правильный ответ сгенерированных
# ранее рандомных чисел
def correct_result(random_num_1, chosen_sign, random_num_2):
    if chosen_sign == '+':
        result: int = random_num_1 + random_num_2
    elif chosen_sign == "*":
        result: int = random_num_1 * random_num_2
    elif chosen_sign == "-":
        if random_num_1 >= random_num_2:
            result: int = random_num_1 - random_num_2
        else:
            result: int = random_num_2 - random_num_1
    return result


def question(random_num_1, chosen_sign, random_num_2):
    if chosen_sign == '+' or '*':
        print(f'Question: {random_num_1} {chosen_sign} {random_num_2}')
    else:
        if random_num_1 >= random_num_2:
            print(f'Question: {random_num_1} {chosen_sign} {random_num_2}')
        else:
            print(f'Question: {random_num_2} {chosen_sign} {random_num_1}')


def main():  # выделяем блок кода, который будет работать
    # при запуске скрипта
    greet()
    get_user_name()
    name = get_user_name()  # определяем переменную name, что бы далее
    # ее просто использовать, а не спрашивать у пользователя снова
    hello()
    print('What is the result of the expression?')

    i = 0
    while i < 3:

        # random_num_1, chosen_sign, random_num_2 =
        # generate_random_math_operation() - была вот такая строка,
        # но что бы не ругался линтер разбиваем ее на 2:
        (random_num_1, chosen_sign, random_num_2) = \
            generate_random_math_operation()

        result = correct_result(random_num_1, chosen_sign, random_num_2)

        question(random_num_1, chosen_sign, random_num_2)

        answer = int(user_answer())

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
