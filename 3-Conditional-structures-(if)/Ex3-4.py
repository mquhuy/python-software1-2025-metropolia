def get_input_integer(var_name, unit=""):
    prompt = f"Enter the {var_name}"
    if unit != "":
        prompt += f"({unit})"
    while True:
        number_str = input(f"{prompt}: ")
        try:
            number = int(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct integer. Please try again!")


def main():
    year = get_input_integer("year")
    is_leap_year = False
    if year % 400 == 0:
        is_leap_year = True
    elif year % 100 != 0 and year % 4 == 0:
        is_leap_year = True

    print(f"Year {int(year)} is{'' if is_leap_year else ' not'} a leap year")


if __name__ == "__main__":
    main()
