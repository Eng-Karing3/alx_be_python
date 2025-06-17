# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to parse command line arguments and perform division
    using the safe_divide function.
    """
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1) # Exit with a non-zero status code to indicate an error

    # Get the numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function to perform the division with error handling
    result = safe_divide(numerator, denominator)
    
    # Print the result or error message returned by safe_divide
    print(result)

if __name__ == "__main__":
    main()

