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
            length = int(input("Length of equation (1, 2, 3): "))

            if length == 1 or length == 2 or length == 3:
                return length
            
            else:
                print("Invalid Length")
                

        except ValueError:
            print("Invalid number of length.")

def get_number(length_of_equation):
    if length_of_equation == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        return(x, y)
    
    elif length_of_equation == 2:
        x = random.randint(00, 99)
        y = random.randint(00, 99)

        return(x, y)

    elif length_of_equation == 3:
        x = random.randint(000, 999)
        y = random.randint(000, 999)

        return(x, y)



if __name__ == "__main__":
    main()