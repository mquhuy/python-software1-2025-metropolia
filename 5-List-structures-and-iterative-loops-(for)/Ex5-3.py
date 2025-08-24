def get_input_integer(var_name):
    while True:
        number_str = input(f"Enter the {var_name}: ")
        try:
            number = int(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct integer. Please try again!")


def is_prime(n):
    """
    Checks if the provided n is a prime number
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    n = get_input_integer("number")
    print(f"{n} is {'' if is_prime(n) else 'not '}a prime number")


if __name__ == "__main__":
    main()
