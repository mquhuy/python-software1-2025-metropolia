def main():
    numbers = []
    while True:
        n_str = input("Please enter a number. Enter empty string to stop: ")
        if n_str == "":
            break
        try:
            number = int(n_str)
            numbers.append(number)
        except ValueError:
            print("Only valid integers are accepted")

    if len(numbers) < 5:
        print("You did not enter enough numbers. We need at least 5.")
        return
    numbers.sort(reverse=True)
    print("Five largest numbers. Sorting from largest:")
    for i in range(5):
        print(f"Number {i + 1}: {numbers[i]}")


if __name__ == "__main__":
    main()
