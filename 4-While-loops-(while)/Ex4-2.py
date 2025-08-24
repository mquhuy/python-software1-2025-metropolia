print("CONVERSION OF INCHES TO CENTIMETERS")
while True:
    n_str = input("Please enter the number of inches. Enter negative value to stop: ")
    try:
        n_inches = float(n_str)
        if n_inches < 0:
            print("GOODBYE!")
            break
        print(f"{n_inches} inches equals {n_inches * 2.54} centimeters.")
    except ValueError:
        print("Only valid float numbers are accepted")
