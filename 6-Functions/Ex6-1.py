import random


def roll_die():
    return random.randint(1, 6)


def main():
    while True:
        die = roll_die()
        print(die)
        if die == 6:
            return


if __name__ == "__main__":
    main()
