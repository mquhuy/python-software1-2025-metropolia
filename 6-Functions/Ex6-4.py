import random


def get_sum(numbers: list) -> int:
    sum = 0
    for n in numbers:
        sum += n
    return sum


def main():
    numbers = [random.randint(1, 100) for _ in range(100)]
    print(f"Result using our custom function: {get_sum(numbers)}")
    # Verify
    print(f"Result using python builtin function: {sum(numbers)}")


if __name__ == "__main__":
    main()
