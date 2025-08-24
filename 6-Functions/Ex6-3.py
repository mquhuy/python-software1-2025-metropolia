def convert_us_gallons_to_liters(volumes_in_gallons):
    return volumes_in_gallons * 3.78541


print("CONVERSION OF U.S. GALLONS TO LITERS")
while True:
    n_str = input(
        "Please enter the number of US gallons. Enter negative value to stop: "
    )
    try:
        n_gallons = float(n_str)
        if n_gallons < 0:
            print("GOODBYE!")
            break
        print(
            f"{n_gallons} US gallons equals {convert_us_gallons_to_liters(n_gallons)} liters."
        )
    except ValueError:
        print("Only valid float numbers are accepted")
