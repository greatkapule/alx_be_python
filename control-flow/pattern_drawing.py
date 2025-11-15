# Filename: pattern_drawing.py

try:
    size = int(input("Enter the size of the pattern: "))
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

row_counter = 0

while row_counter < size:
    
    for column_counter in range(size):
        # Print asterisk without a newline
        print("*", end="")
        
    print()
    
    # Increment the row counter to move to the next iteration
    row_counter += 1