import math

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

def calculate_pizza_price_per_squared_meter(diameter, price):
    """
    Return the price per squared meter of the pizza
    """
    radius = diameter/2
    radius_in_meter = radius/100
    area = (radius_in_meter**2)*math.pi
    return price/area


def main():
    ppsm_dict = {}
    pizza_names = ["First", "Second"]
    for pizza in pizza_names:
        p = {}
        for value in ["diameter", "price"]:
            p[value] = get_input_number(f"{pizza} pizza {value}")
        ppsm_dict[pizza] = calculate_pizza_price_per_squared_meter(p["diameter"], p["price"])

    first_ppsm = ppsm_dict["First"]
    second_ppsm = ppsm_dict["Second"]

    if first_ppsm == second_ppsm:
        print("Two pizzas provide equal value for money.")
    else:
        better_pizza = "first" if first_ppsm > second_ppsm else "second"
        print(f"The {better_pizza} pizza provides better value for money.")

if __name__ == "__main__":
    main()
