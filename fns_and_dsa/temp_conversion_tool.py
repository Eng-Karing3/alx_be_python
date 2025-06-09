
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__ == "__main__":
    temperature_input_str = ""
    unit_input = ""

    
    try:
       
        temperature_input_str = input("Enter the temperature to convert: ")
        temperature = float(temperature_input_str)

        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_input == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit_input == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:

            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        
        raise ValueError("Invalid temperature. Please enter a numeric value.")