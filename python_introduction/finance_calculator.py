# --- Define Constants ---
ANNUAL_RATE = 0.05  # 5% annual interest rate
MONTHS_IN_YEAR = 12
# 1. User Input (We use float() to handle potential decimal inputs)
# Get monthly income and immediately convert it from string to float
monthly_income = float(input("Enter your monthly income: "))
# Get monthly expenses and convert to float
monthly_expenses = float(input("Enter your total monthly expenses: "))
# --- 2. Calculate Monthly Savings ---
monthly_savings = monthly_income - monthly_expenses
# --- 3. Project Annual Savings (with interest) ---
# Calculate savings over 12 months without interest
annual_savings_base = monthly_savings * MONTHS_IN_YEAR
# Calculate the simple interest earned on the annual savings
# Formula: Base Savings * Annual Rate
interest_earned = annual_savings_base * ANNUAL_RATE
# Calculate the final projected total savings
projected_savings = annual_savings_base + interest_earned
# --- 4. Output Results ---
# Display the monthly savings
# Note: Using :.2f ensures the output looks like currency (e.g., 1000.00)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
# Display the projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")