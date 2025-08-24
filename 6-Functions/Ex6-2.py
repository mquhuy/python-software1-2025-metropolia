import random


def roll_die(n_sides):
    if n_sides < 1:
        raise ValueError("Wrong number of sides")
    return random.randint(1, n_sides)


def get_n_sides():
    while True:
        n_sides_str = input("Please enter number of sides: ")
        try:
            n_sides = int(n_sides_str)
            return n_sides
        except ValueError:
            print("Only valid integers are accepted")


def main():
    n_sides = get_n_sides()
    while True:
        die = roll_die(n_sides)
        print(die)
        if die == n_sides:
            return


if __name__ == "__main__":
    main()
