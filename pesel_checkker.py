from pesel_generator import generate_pesel
from user_input import user_input


def pesel_checker():
    formula_digits = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    pesel_bool = False
    pesel_to_check = ''

    birth_date = user_input()

    while not pesel_bool:
        pesel_to_check = generate_pesel(birth_date)
        checking = 0

        for i in range(len(pesel_to_check)):
            checking += int(pesel_to_check[int(i)]) * formula_digits[i]

        checking = int(checking)

        if checking % 10 == 0:
            pesel_bool = True
        else:
            pesel_bool = False

    return pesel_to_check


print(pesel_checker())

