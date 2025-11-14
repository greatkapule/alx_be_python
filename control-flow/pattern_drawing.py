# pattern_drawing.py

def main():
    size_str = input("Enter the size of the pattern: ")

    try:
        size = int(size_str)
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    row = 0
    while row < size:
        # Print `size` asterisks on the same line
        for _ in range(size):
            print("*", end="")
        print()  # move to the next line after finishing the row
        row += 1


if __name__ == "__main__":
    main()