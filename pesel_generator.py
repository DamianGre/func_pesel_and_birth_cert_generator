from number_generator import generate_five_number

def generate_pesel(year, month, day):

    if len(str(month)) == 1:
        month = str('0' + str(month))

    pesel = str(year)[-2:] + str(month) + str(day) + str(generate_five_number())

    return pesel
