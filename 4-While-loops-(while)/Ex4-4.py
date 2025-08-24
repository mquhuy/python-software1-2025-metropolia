from random import randint


def main():
    number = randint(1, 10)
    while True:
        guess = input("Please enter your guess (integer between 1 and 10): ")
        try:
            guess_num = int(guess)
            if guess_num == number:
                print("Correct")
                return
            elif guess_num < number:
                print("Too low")
            elif guess_num > number:
                print("Too high")
        except ValueError:
            print("Only valid integers are accepted.")


if __name__ == "__main__":
    main()
