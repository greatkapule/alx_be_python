# weather_advice.py

# 1. Prompt User for Weather Input and normalize it
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# 2. Provide Clothing Recommendations using if-elif-else
# USE SINGLE QUOTES ('') FOR ALL OUTPUT STRINGS

if weather == "sunny":
    # Changed from "..." to '...'
    print('Wear a t-shirt and sunglasses.')

elif weather == "rainy":
    # Changed from "..." to '...'
    print('Don\'t forget your umbrella and a raincoat.') # Note the escaped quote here

elif weather == "cold":
    # Changed from "..." to '...'
    print('Make sure to wear a warm coat and a scarf.')

else:
    # Changed from "..." to '...'
    print('Sorry, I don\'t have recommendations for this weather.')