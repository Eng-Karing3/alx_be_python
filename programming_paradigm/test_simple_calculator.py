# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    """
    Test class for the SimpleCalculator.
    Inherits from unittest.TestCase to provide testing capabilities.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method of SimpleCalculator for various scenarios.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

        # Test with negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, -3), -8)

        # Test with positive and negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -2), 3)
        self.assertEqual(self.calc.add(-10, 7), -3)

        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

        # Test with floating-point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-1.5, 2.0), 0.5)

    def test_subtract(self):
        """
        Test the subtract method of SimpleCalculator for various scenarios.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, 4), 6)

        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-1, -5), 4)

        # Test with positive and negative numbers
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(-5, 2), -7)

        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # Test with floating-point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(2.0, 1.5), 0.5)

    def test_multiply(self):
        """
        Test the multiply method of SimpleCalculator for various scenarios.
        """
        # Test with positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 0.5), 5.0)

        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(5, -2), -10)

        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

        # Test with floating-point numbers
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(1.5, 1.5), 2.25)

    def test_divide(self):
        """
        Test the divide method of SimpleCalculator for various scenarios,
        including division by zero.
        """
        # Test with normal positive division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

        # Test with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

        # Test division resulting in a float
        self.assertEqual(self.calc.divide(1, 3), 1/3)

        # Test division by zero (edge case)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Even 0/0 should return None as per method docstring.

        # Test dividing zero by a non-zero number
        self.assertEqual(self.calc.divide(0, 5), 0.0)


# This block allows you to run the tests directly from the command line.
if __name__ == '__main__':
    unittest.main()

