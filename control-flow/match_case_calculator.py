# match_case_calculator.py

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation
match operation:
    case "+":
        result = number1 + number2
        print(f"The result is {result}.")
    case "-":
        result = number1 - number2
        print(f"The result is {result}.")
    case "*":
        result = number1 * number2
        print(f"The result is {result}.")
    case "/":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            result = number1 / number2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")