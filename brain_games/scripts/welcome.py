import prompt


def greet():
    print('Welcome to the Brain Games!')


user_name = None  # определили переменную user_name как None


def get_user_name():  # Ф-я сейчас проверяет, есть ли имя в перем-й user_name.
    # Если нет, то она запрашивает имя у пользователя и
    # сохраняет его в переменной user_name.
    # Если имя уже есть, то она возвращает текущее имя.
    global user_name
    if user_name is None:
        user_name = prompt.string('May I have your name? ')
    return user_name


def hello():
    name = get_user_name()
    print(f'Hello, {name}!')


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def yuhoo():
    name = get_user_name()
    print(f'Congratulations, {name}!')
