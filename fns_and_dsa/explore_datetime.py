
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date

def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        time_difference = timedelta(days=days_to_add)

        future_date = current_date + time_difference

        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("Invalid input. Please enter a whole number for the number of days.")

def main():

    current_datetime_object = display_current_datetime()

    calculate_future_date(current_datetime_object)

if __name__ == "__main__":
    main()