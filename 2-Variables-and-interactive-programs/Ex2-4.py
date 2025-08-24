def get_input_number(var_name):
    while True:
        number_str = input(f"Please enter the {var_name}:")
        try:
            number = float(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct float number. Please try again!")

def main():
    sum = 0.0
    product = 1.0
    for var_name in ["first number", "second number", "third number"]:
        num = get_input_number(var_name)
        sum += num
        product *= num

    print(f"Sum: {sum}. Product: {product}. Average: {sum/3}")

if __name__ == "__main__":
    main()
