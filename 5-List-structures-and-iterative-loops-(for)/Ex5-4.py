def main():
    cities = []
    for idx in range(5):
        new_city = input(f"Please enter name of city number {idx + 1}")
        cities.append(new_city)

    for city in cities:
        print(city)

if __name__ == "__main__":
    main()
