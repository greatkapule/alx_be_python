# match_case_calculator.py

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

operation = input("Choose the operation (+, -, *, /): ")
result = None

# Perform the Calculation Using Match Case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        # Handle division by zero gracefully
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            exit()
    case _:
        # Default case for invalid operations
        print(f"Invalid operation: {operation}. Please choose +, -, *, or /.")
        exit()

# Output the Result
print(f"The result is {result}")
