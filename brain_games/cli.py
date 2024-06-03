import prompt

def get_user_name():
    name = prompt.string('May I have your name? ')
    return name

def welcome_user():
    name = get_user_name()
    print(f'Hello, {name}!')

