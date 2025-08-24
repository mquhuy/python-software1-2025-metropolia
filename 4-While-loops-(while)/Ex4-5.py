USERNAME = "python"
PASSWORD = "rules"


def main():
    counter = 5
    while counter > 0:
        username = input("Please input username: ")
        password = input("Please input password: ")
        if username == USERNAME and password == PASSWORD:
            print("Welcome.")
            return
        counter -= 1
    print("Access denied")


if __name__ == "__main__":
    main()
