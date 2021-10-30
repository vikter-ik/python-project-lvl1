import prompt


def welcome():
    return "Welcome to the Brain Games!"


def get_user_name():
    name = prompt.string("May I have your name? ")
    return name


def welcome_user(name):
    return "Hello, {}!".format(name)


def get_answer(q_string):
    return prompt.string(q_string)
