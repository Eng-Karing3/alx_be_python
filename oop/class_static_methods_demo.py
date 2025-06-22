class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of a and b and print the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b