import random


def get_input_integer(var_name):
    while True:
        number_str = input(f"Enter the {var_name}: ")
        try:
            number = int(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct integer. Please try again!")


def main():
    n_dice = get_input_integer("number of dice")
    sum_of_numbers = 0
    for _ in range(n_dice):
        sum_of_numbers += random.randint(1, 6)
    print(f"Sum of all {n_dice} dice is: {sum_of_numbers}")


if __name__ == "__main__":
    main()
