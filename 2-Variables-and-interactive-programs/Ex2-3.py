def get_input_number(var_name):
    while True:
        number_str = input(f"Please enter the {var_name}:")
        try:
            number = float(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct float number. Please try again!")

def main():
    while True:
        length = get_input_number("length")
        width = get_input_number("width")
        if length >= width:
            break
        print("Length should not be smaller than width!")

    print(f"Perimeter: {(length+width)*2}. Area: {length*width}")

if __name__ == "__main__":
    main()
