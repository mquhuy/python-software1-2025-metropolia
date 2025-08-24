import random


def remove_uneven(numbers: list) -> list:
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


def main():
    numbers = [random.randint(1, 100) for _ in range(100)]
    print(f"Original list: {numbers}")
    print(f"Cut-down list: {remove_uneven(numbers)}")


if __name__ == "__main__":
    main()
