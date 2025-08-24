def get_input_number(var_name):
    while True:
        number_str = input(f"Enter the {var_name}:")
        try:
            number = float(number_str)
            return number
        except ValueError:
            print(f"{number_str} is not a correct float number. Please try again!")

def main():
    mass = {}
    for var_name in ["talents", "pounds", "lots"]:
        num = get_input_number(var_name)
        mass[var_name] = num

    pounds = mass["talents"]*20 + mass["pounds"]
    lots = pounds + mass["lots"]
    mass_in_g = lots*13.3

    mass_in_kg = mass_in_g//1000
    mass_in_g -= mass_in_kg*1000
    
    modern = ""
    if mass_in_kg > 0:
        modern += f"{mass_in_kg} kg"
    if mass_in_g > 0 and len(modern) > 0:
        modern += f" and {mass_in_g} g"
    elif mass_in_g > 0:
        modern = f"{mass_in_g} g"

    print("The weight in modern units:")
    print(f"{modern}.")

if __name__ == "__main__":
    main()
