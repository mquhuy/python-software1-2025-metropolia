def main():
    airports = {}
    while True:
        print("""Choose your operation: 
    1. Enter new airport
    2. Fetch the airport
    3. Quit""")
        operation = input("Your choice [1/2/3]: ")
        if operation == "1":
            icao = input("ICAO: ")
            airport = input("Airport name: ")
            airports[icao] = airport
            print("Update successfully")
        elif operation == "2":
            icao = input("ICAO: ")
            if airports.get(icao) is not None:
                print(f"Airport name of {icao} is {airports[icao]}")
                continue
            print("This ICAO is not in the database yet")
        elif operation == "3":
            return
        else:
            print("ERROR: Incorrect operation")

if __name__ == "__main__":
    main()
