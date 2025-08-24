def main():
    numbers = []
    while True:
        n_str = input("Please enter the number. Enter empty string to stop: ")
        if n_str == "":
            break
        try:
            number = float(n_str)
            numbers.append(number)
        except ValueError:
            print("Only valid float numbers are accepted")

    if len(numbers) == 0:
        print("You did not enter any number.")
        return
    print(f"Smallest number: {min(numbers)}. Largest number: {max(numbers)}")


if __name__ == "__main__":
    main()
