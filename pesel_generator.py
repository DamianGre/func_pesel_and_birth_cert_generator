from number_generator import generate_five_number
from user_input import user_input


def generate_pesel(birth_date):

    if len(str(birth_date[1])) == 1:
        birth_date[1] = str('0' + str(birth_date[1]))

    if len(str(birth_date[2])) == 1:
        birth_date[2] = str('0' + str(birth_date[2]))

    pesel = str(birth_date[0])[-2:] + str(birth_date[1]) + str(birth_date[2]) + str(generate_five_number())

    return pesel

