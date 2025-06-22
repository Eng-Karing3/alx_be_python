<<<<<<< HEAD
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
=======
#!/usr/bin/env python3
"""
This script tests the functionality of the Book, EBook, PrintBook,
and Library classes defined in library_system.py.
It demonstrates creating various book types, adding them to a library,
and then listing all the books.
"""

from library_system import Book, EBook, PrintBook, Library

def main():
    """
    Main function to demonstrate the library system.
    """
    # Create a Library instance
    my_library = Library()
>>>>>>> ea89a551589161b60f4ac82dc4f4e4aba7aa498c

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
