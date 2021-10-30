#!/usr/bin/env python
from brain_games.cli import (
    welcome,
    get_user_name,
    welcome_user
)
from brain_games.games import gen_calc_game, play_game


def main():
    print(welcome())
    name = get_user_name()

    print(welcome_user(name))

    statement = 'What is the result of the expression?'
    play_game(gen_calc_game, statement, name)


if __name__ == "__main__":
    main()
