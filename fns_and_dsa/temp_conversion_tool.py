FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):

    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return c * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def _interactive_prompt():
    import sys

    original = input("Enter the temperature to convert: ").strip()
    try:
        _ = float(original)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit in ("F", "FAHRENHEIT"):
        converted = convert_to_celsius(original)
        print(f"{float(original)}°F is {converted}°C")
    elif unit in ("C", "CELSIUS"):
        converted = convert_to_fahrenheit(original)
        print(f"{float(original)}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        _interactive_prompt()
    except ValueError as e:
        import sys

        print(e, file=sys.stderr)
        sys.exit(1)
