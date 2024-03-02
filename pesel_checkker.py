from pesel_generator import generate_pesel
from number_generator import generate_five_number

def pesel_checkker():
    forumla_digits = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    pesel_bool = False
    pesel_to_check = ''

    while pesel_bool == False:
        pesel_to_check = generate_pesel(1990, 4, 26)
        checking = 0

        for i in range(len(pesel_to_check)):
            checking += int(pesel_to_check[int(i)]) * forumla_digits[i]

        checking = int(checking)


        if checking % 10 == 0:
            pesel_bool = True
        else:
            pesel_bool = False

    return pesel_to_check

print(pesel_checkker())
