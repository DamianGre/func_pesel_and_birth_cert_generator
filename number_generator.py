import random


def generate_five_number():
    five_number = ''
    for i in range(5):
        five_number += str(random.randint(0, 9))

    return five_number






