# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling potential errors like
    ZeroDivisionError and ValueError for non-numeric inputs.

    Args:
        numerator (str): The string representation of the numerator.
        denominator (str): The string representation of the denominator.

    Returns:
        str: A message indicating the result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        # Catch non-numeric input errors during float conversion
        return "Error: Please enter numeric values only."
    # No need for a separate ZeroDivisionError catch here because we explicitly
    # check for denominator == 0 after successful float conversion.
    # If the conversion fails, ValueError is caught first.

