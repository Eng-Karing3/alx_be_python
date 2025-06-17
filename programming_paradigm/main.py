

from library_management import Book, Library

def main():
    """
    Demonstrates the functionality of the Library and Book classes.
    """
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald")) # Adding another book for more testing

    # Initial list of available books
    print("\n--- Available books after initial setup ---")
    library.list_available_books()

    # Simulate checking out a book
    print("\n--- Checking out '1984' ---")
    library.check_out_book("1984")
    print("\n--- Available books after checking out '1984' ---")
    library.list_available_books()

    # Try to check out a book that's already checked out
    print("\n--- Attempting to check out '1984' again ---")
    library.check_out_book("1984")

    # Try to check out a book that doesn't exist
    print("\n--- Attempting to check out 'Nonexistent Book' ---")
    library.check_out_book("Nonexistent Book")

    # Simulate returning a book
    print("\n--- Returning '1984' ---")
    library.return_book("1984")
    print("\n--- Available books after returning '1984' ---")
    library.list_available_books()

    # Try to return a book that was not checked out
    print("\n--- Attempting to return 'Brave New World' (not checked out) ---")
    library.return_book("Brave New World")

    # Check out and return multiple times
    print("\n--- Checking out 'The Great Gatsby' ---")
    library.check_out_book("The Great Gatsby")
    print("\n--- Available books after checking out 'The Great Gatsby' ---")
    library.list_available_books()
    print("\n--- Returning 'The Great Gatsby' ---")
    library.return_book("The Great Gatsby")
    print("\n--- Available books after returning 'The Great Gatsby' ---")
    library.list_available_books()


if __name__ == "__main__":
    main()

