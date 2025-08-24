MINIMUM_ZANDER_LENGTH_LIMIT_IN_CENTIMETERS = 42


def get_input_number(var_name):
    while True:
        number_str = input(f"Enter the {var_name}: ")
        try:
            number = float(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct float number. Please try again!")


def main():
    zander_length = get_input_number("zander length in centimeters")
    if zander_length < MINIMUM_ZANDER_LENGTH_LIMIT_IN_CENTIMETERS:
        print(
            f"Please release the zander. It's {MINIMUM_ZANDER_LENGTH_LIMIT_IN_CENTIMETERS - zander_length} centimeters under the limit."
        )

if __name__ == "__main__":
    main()
