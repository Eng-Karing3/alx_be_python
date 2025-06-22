#!/usr/bin/env python3
"""
This script defines a class hierarchy for different types of books
(Book, EBook, PrintBook) demonstrating inheritance, and a Library class
that manages a collection of these books, showcasing composition.
"""

class Book:
    """
    Base class for a generic book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for an electronic book, inheriting from Book.
    Additional Attributes:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in kilobytes (KB).
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object,
        including its file size.
        """
        # Reuse the base class's string and add specific details
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for a physical print book, inheriting from Book.
    Additional Attributes:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object,
        including its page count.
        """
        # Reuse the base class's string and add specific details
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library that manages a collection of books.
    This demonstrates the concept of composition.

    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (can be Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book instances (or derived classes) can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        It utilizes the __str__ method of each book object.
        """
        if not self.books:
            print("The library currently has no books.")
            return

        print("\n--- Books in the Library ---")
        for book in self.books:
            # The print() function automatically calls the __str__ method
            # of the respective book object (Book, EBook, or PrintBook).
            print(book)
        print("----------------------------")


