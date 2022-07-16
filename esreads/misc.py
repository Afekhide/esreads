from random import randint


def generate_api_key():
    first_part = str(randint(1, 9)) + str(randint(0, 9)) + '-'
    second_part = [str(randint(0, 9)) for i in range(7)]
    return first_part + ''.join(second_part)

