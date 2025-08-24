def main():
    names = set()
    while True:
        name = input("Please enter the name. Enter empty string to stop: ")
        if name == "":
            break
        if name in names:
            print("Existing name")
            continue
        print("New name")
        names.add(name)

    for name in names:
        print(name)


if __name__ == "__main__":
    main()
