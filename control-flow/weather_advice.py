# weather_advice.py

# 1. Prompt User for Weather Input and immediately normalize it
# This line performs the prompt, removes any leading/trailing spaces, and converts to lowercase.
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# 2. Provide Clothing Recommendations using if-elif-else

if weather == "sunny":
    # Output must match exactly (Note the period)
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    # Output must match exactly (Note the period)
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    # Output must match exactly (Note the period)
    print("Make sure to wear a warm coat and a scarf.")

else:
    # Output must match exactly (Note the period)
    print("Sorry, I don't have recommendations for this weather.")