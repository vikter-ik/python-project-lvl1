import random


from brain_games.cli import get_answer


def gen_even_game():
    num = random.randint(1, 1000)

    answer = "yes" if num % 2 == 0 else "no"
    return (str(num), answer)


def gen_calc_game():
    a, b = random.randint(1, 1000), random.randint(1, 1000)

    f, str_f = random.choice([
        (lambda x, y: x + y, '+'),
        (lambda x, y: x - y, '-'),
        (lambda x, y: x + y, '*')]
    )

    question = "{} {} {}".format(a, str_f, b)
    answer = str(f(a, b))
    return (question, answer)


def gen_gcd_game():
    a, b = random.randint(1, 100), random.randint(1, 100)

    if a < b:
        a, b = b, a
    question = "{} {}".format(a, b)

    while a % b > 0:
        a, b = b, a % b

    answer = str(b)
    return (question, answer)


def gen_progression_game():
    n = random.randint(5, 15)
    a_0 = random.randint(1, 25)

    step = random.randint(1, 25)
    sequence = [str(a_0 + i * step) for i in range(n)]

    position = random.randint(0, n - 1)
    answer = str(sequence[position])
    sequence[position] = '..'

    question = ' '.join(sequence)
    return (question, answer)


def play_game(gen_game, start_statement, name):
    print(start_statement)
    count = 0

    while count < 3:
        question, correct_answer = gen_game()

        print("Question: {}".format(question))
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
