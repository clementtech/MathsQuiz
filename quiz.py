import sys

print("Welcome to Math Quiz!")
print("Please select the type of quiz.")


def main():
    equation = get_equation()
    length_of_equation = get_length()

    print(equation, length_of_equation)


def get_equation():
    while True:
        print("Please select '+' or '-' or '*' or '/'")
        equation = input(str("Equation: "))

        if equation != "+" and equation != "-" and equation != "*" and equation != "/":
            print("Invalid equation.")

        elif equation == "+" or equation == "-" or equation == "*" or equation == "/":
            return equation

def get_length():
    while True:
        try:
            return int(input("Length of equation: "))

        except ValueError:
            print("Invalid number of length.")


if __name__ == "__main__":
    main()