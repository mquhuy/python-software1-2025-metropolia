from math import pi
import sys

while True:
    radius_str = input("Please enter the radius:")
    try:
        radius = float(radius_str)
        print(f"Area of the circle: {radius**2*pi}")
        sys.exit(0)
    except ValueError:
        print(f"{radius_str} is not a correct float number. Please try again!")
