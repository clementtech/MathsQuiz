import sys
import random

print("Welcome to Math Quiz!")
print("Please select the type of quiz.")


def main():
    equation = get_equation()
    length_of_equation = get_length()
    number = get_number(length_of_equation)

    print(equation, length_of_equation, number)


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
            length = int(input("Length of equation (1, 2, ..., 10): "))

            if 1 <= length <= 10:
                return length
            
            else:
                print("Invalid Length")
                

        except ValueError:
            print("Invalid number of length.")

def get_number(length_of_equation):
    if length_of_equation == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        return (x, y)

    elif length_of_equation == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

        return (x, y)

    elif length_of_equation == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

        return (x, y)

    elif length_of_equation == 4:
        x = random.randint(1000, 9999)
        y = random.randint(1000, 9999)

        return (x, y)

    elif length_of_equation == 5:
        x = random.randint(10000, 99999)
        y = random.randint(10000, 99999)

        return (x, y)

    elif length_of_equation == 6:
        x = random.randint(100000, 999999)
        y = random.randint(100000, 999999)

        return (x, y)

    elif length_of_equation == 7:
        x = random.randint(1000000, 9999999)
        y = random.randint(1000000, 9999999)

        return (x, y)

    elif length_of_equation == 8:
        x = random.randint(10000000, 99999999)
        y = random.randint(10000000, 99999999)

        return (x, y)

    elif length_of_equation == 9:
        x = random.randint(100000000, 999999999)
        y = random.randint(100000000, 999999999)

        return (x, y)

    elif length_of_equation == 10:
        x = random.randint(1000000000, 9999999999)
        y = random.randint(1000000000, 9999999999)

        return (x, y)



if __name__ == "__main__":
    main()