SEASONS = ("Spring", "Summer", "Autumn", "Winter")


def get_month_number_from_input():
    while True:
        month_number_str = input("Please enter the month number [1-12]: ")
        try:
            month_number = int(month_number_str)
            if month_number > 12 or month_number < 1:
                raise ValueError("Invalid month")
            return month_number
        except ValueError:
            print("Only valid integers in range 01-12 are accepted.")


def get_season_from_month_number(month_number):
    # Convert to 0-index
    month_number -= 1

    # Convert March-start year to January-start year
    month_number -= 2
    if month_number < 0:
        month_number += 12

    season_idx = month_number // 3
    return SEASONS[season_idx]


def main():
    month_number = get_month_number_from_input()
    print(get_season_from_month_number(month_number))


if __name__ == "__main__":
    main()
