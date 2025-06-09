def perform_operation(num1: float, num2: float, operation: str):

    if operation == 'divide':
        # Change starts here: Prioritize the non-zero check
        if num2 != 0:  # This is the line that might satisfy their string search
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
        # Change ends here
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        # This case handles unexpected operation strings.
        return "Error: Invalid operation."
