def get_input_number(var_name, unit=""):
    prompt = f"Enter the {var_name}"
    if unit != "":
        prompt += f"({unit})"
    while True:
        number_str = input(f"{prompt}: ")
        try:
            number = float(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct float number. Please try again!")


def get_input_with_options(var_name, options=[]):
    # If options is empty, any value is acceptable
    prompt = f"Please enter {var_name}"
    if len(options) > 0:
        prompt += f" [{'/'.join(options)}]"
    prompt += ": "
    options = [o.upper() for o in options]
    while True:
        value = input(prompt)
        value = value.upper()
        if len(options) == 0 or value in options:
            return value
        print(f"Only accept following options: {', '.join(options)}")


def main():
    gender = get_input_with_options("biological gender", ["m", "f"])
    hemoglobin_value = get_input_number("hemoglobin value", "g/l")
    acceptable_hemo_range = {
        "M": [117, 155],
        "F": [134, 167],
    }
    if hemoglobin_value < acceptable_hemo_range[gender][0]:
        print("Your hemoglobin is rather low.")
    elif hemoglobin_value > acceptable_hemo_range[gender][1]:
        print("Your hemoglobin is too high.")
    else:
        print("Your hemoglobin is normal.")


if __name__ == "__main__":
    main()
