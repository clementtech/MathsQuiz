import sys

print("Welcome to Math Quiz!")
print("Please select the type of quiz.")


def main():
    print(get_equation())


def get_equation():
    while True:
        print("Please select '+' or '-' or '*' or '/'")
        equation = input(str("Equation: "))

        if equation != "+" and equation != "-" and equation != "*" and equation != "/":
            print("Invalid equation.")

        elif equation == "+" or equation == "-" or equation == "*" or equation == "/":
            return equation



if __name__ == "__main__":
    main()