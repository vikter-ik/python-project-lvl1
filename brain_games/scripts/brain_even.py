#!/usr/bin/env python
import random


from brain_games.cli import (
    welcome,
    get_user_name,
    welcome_user,
    get_answer
)


def main():
    print(welcome())
    name = get_user_name()

    print(welcome_user(name))
    play_game(name)


def play_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        num = random.randint(1, 100)
        print("Question: {}".format(num))

        correct_answer = "yes" if num % 2 == 0 else "no"
        answer = get_answer("Your answer: ")

        if answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, correct_answer))

            print("Let's try again, {}!".format(name))
            return None
        count += 1
        print("Correct!")

    print("Congratulations, {}!".format(name))
    return None


if __name__ == "__main__":
    main()
