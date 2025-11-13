# weather_advice.py

# 1. Prompt User for Weather Input
# in a variable called 'weather'. We also convert the input to lowercase
# using .lower() to make the check case-insensitive (e.g., 'Sunny' becomes 'sunny').
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Provide Clothing Recommendations using if-elif-else

# The 'if' statement checks the first condition.
if weather == "sunny":
    # 3. Output the Recommendation
    print("Wear a t-shirt and sunglasses.")

# The 'elif' (else if) statement checks the next condition only if the 'if' was False.
elif weather == "rainy":
    # 3. Output the Recommendation
    print("Don't forget your umbrella and a raincoat.")

# The second 'elif' checks the third condition.
elif weather == "cold":
    # 3. Output the Recommendation
    print("Make sure to wear a warm coat and a scarf.")

# The 'else' statement runs if NONE of the preceding 'if' or 'elif' conditions were True.
else:
    # 3. Output the Recommendation for unexpected input
    print("Sorry, I don't have recommendations for this weather.")