from datetime import datetime, timedelta 

# Get the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

#  Calculating future date by adding days 
def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    print(f"Date after {days} days: {future_date.strftime('%Y-%m-%d')}")
    return future_date

current_date = display_current_datetime()
days =int(input("Enter the number of days to add to the current date: "))
calculate_future_date(current_date, days)