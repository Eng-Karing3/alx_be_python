

class Book:
    """
    Represents a single book in the library system.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): A private attribute indicating if the book is currently checked out.
    """

    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute, default to not checked out

    def check_out(self):
        """
        Marks the book as checked out.
        Returns True if successful, False if already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as returned (available).
        Returns True if successful, False if already available.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances.
    """

    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class to be added.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"'{book.title}' added to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """
        Helper method to find a book by its title in the library's collection.

        Args:
            title (str): The title of the book to find.

        Returns:
            Book or None: The Book object if found, otherwise None.
        """
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"Book '{title}' checked out successfully.")
            else:
                print(f"Book '{title}' is already checked out.")
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"Book '{title}' returned successfully.")
            else:
                print(f"Book '{title}' was not checked out.")
        else:
            print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints the titles and authors of all books currently available in the library.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found:
            print("No books are currently available.")

