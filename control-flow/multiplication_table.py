# multiplication_table.py

def main():

    number_str = input("Enter a number to see its multiplication table: ")

    try:
        number = int(number_str)
    except ValueError:
        print("Please enter a valid integer.")
        return

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


if __name__ == "__main__":
    main()

