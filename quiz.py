import sys
import random

print("=" * 30)
print(" Welcome to Math Quiz! ".center(30, "="))
print("=" * 30)
print("Please select the type of quiz.")


def main():
    equation = get_equation()
    length_of_equation = get_length()
    number = get_number(length_of_equation)
    ai_consent = get_ai_consent()
    question = get_question()

    print(f"Equation: {equation}")
    print(f"Length of Equation: {length_of_equation}")
    print(f"Numbers: {number}")
    print(f"AI Consent: {ai_consent}")

def get_equation():
    while True:
        print("Please select one of the following operations: +, -, *, /")
        equation = input(str("Equation: "))

        if equation in ["+", "-", "*", "/"]:
            return equation
        else:
            print("Invalid equation. Please choose one of +, -, *, /.")

def get_length():
    while True:
        try:
            length = int(input("Enter the length of the equation (choose a number between 1 and 10): "))

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

def get_ai_consent():
    while True:
        consent = input("Do you want Google Gemini to explain the questions to you? (y/n): ").strip().lower()
        if consent in ['y', 'n']:
            return consent == 'y'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def get_question():
    ...

if __name__ == "__main__":
    main()