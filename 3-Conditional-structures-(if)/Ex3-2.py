def main():
    cabin = input("Please enter the cabin class (LUX/A/B/C): ")
    cabin = cabin.upper()
    if cabin == "LUX":
        print("Cabin class LUX: upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Cabin class A: above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Cabin class B: windowless cabin above the car deck.")
    elif cabin == "C":
        print("Cabin class C: windowless cabin below the car deck.")
    else:
        print("ERROR: Invalid cabin class.")


if __name__ == "__main__":
    main()
