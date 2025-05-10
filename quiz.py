import sys

print("Welcome to Math Quiz!")
print("Please select the type of quiz.")


def main():
    while True:
        print("Please select '+' or '-' or '*' or '/'")
        equation = input(str("Equation: "))

        if equation != "+" and equation != "-" and equation != "*" and equation != "/":
            print("Invalid equation.")

        elif equation == "+" or equation == "-" or equation == "*" or equation == "/":
            equation_operator(equation)
            break


def equation_operator(equation):
    print(equation)

if __name__ == "__main__":
    main()