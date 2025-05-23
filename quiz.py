import sys
import random

print("=" * 30)
print(" Welcome to Math Quiz! ".center(30, "="))
print("=" * 30)
print("Please select the type of quiz.")


def main():
    equation = get_equation()
    length_of_equation = get_length()

    print("Good luck! Type 'stop' anytime to end the quiz. Let's get started!")
    while True:
        number_x, number_y = get_number(length_of_equation)
        answer = get_answer(number_x, number_y, equation)

        question = get_question(number_x, number_y, equation, answer)
        if question == False:
            break
    


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
            length = int(input("Enter the length of the equation (choose a number from 1 to 3): "))

            if 1 <= length <= 3:
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

def get_answer(x, y, e):

    if e == "+":
        return (x + y)
    
    elif e == "-":
        return (x - y)

    elif e == "*":
        return (x * y)

    elif e == "/":
        return (x * y)
    
def get_question(x, y, e, a):
    try:

        while True:

            question = str(input((f"{x} {e} {y} = ")))

            if question == "stop":
                return False
            
            else:
                question = int(question)
                if question != a:
                    print("WRONG! Please try again.")

                elif question == a:
                    return True
        
    except ValueError:
        print("Invalid input.")

    
if __name__ == "__main__":
    main()