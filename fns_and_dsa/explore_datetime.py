# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Return current_date for use in the next function

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in "YYYY-MM-DD" format.

    Args:
        current_date (datetime): The starting datetime object from which to calculate.
    """
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            number_of_days = int(days_to_add_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a whole number for days.")

    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date # Optional: return future_date if needed elsewhere


if __name__ == "__main__":
    print("DateTime Operations")

    # Part 1: Display Current Date and Time
    current = display_current_datetime() # Capture the current_date returned

    # Part 2: Calculate a Future Date
    # Pass the captured current_date to the next function
    calculate_future_date(current)