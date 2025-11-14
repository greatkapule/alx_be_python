# 1. Get User Input (The input() function returns text/string)
# We prompt the user with the required question
current_age_str = input("How old are you? ")
# --- 2. Convert Input and Calculate ---
# Python cannot do math with text (strings). We must convert the input
# string to an integer (a whole number) using the int() function.
current_age_int = int(current_age_str)
# Calculate the years difference: 2050 - 2023 = 27
YEARS_TO_ADD = 27
# Calculate the age in 2050
future_age = current_age_int + YEARS_TO_ADD
# --- 3. Print the Result ---
# Print the final result in the specified format
print(f"In 2050, you will be {future_age} years old.")