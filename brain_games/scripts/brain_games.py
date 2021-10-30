#!/usr/bin/env python
from brain_games.cli import welcome, get_user_name, welcome_user


def main():
    print(welcome())
    print(welcome_user(get_user_name()))


if __name__ == "__main__":
    main()
