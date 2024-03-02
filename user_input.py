

def user_input():
    year = 0
    month = 0
    day = 0

    while int(year) > 2024 or int(year) < 1900:
        year = input("Enter year: ")

    while int(month) > 12 or int(month) < 1:
        month = input("Enter month: ")

    while int(day) > 31 or int(day) < 1:
        day = input("Enter day: ")

    birth_date = [int(year), int(month), int(day)]

    return birth_date
