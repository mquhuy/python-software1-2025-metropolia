from random import randint

def generate_combination_lock(length, lower_limit, upper_limit):
    code = ""
    for _ in range(length):
        code += f"{randint(lower_limit, upper_limit)}"
    return code

if __name__ == "__main__":
    print(f"a 3-digit code where each number is between 0 and 9: {generate_combination_lock(3, 0, 9)}")
    print(f"a 4-digit code where each number is between 1 and 6: {generate_combination_lock(4, 1, 6)}")


