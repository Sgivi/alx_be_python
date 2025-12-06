
class Book:
    # A class that represents a single book in the library.

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        # Mark the book as checked out.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        # Mark the book as available again.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # book was not checked out

    def is_available(self):
        # Check if the book is available.
        return not self._is_checked_out


class Library:
    # A class that manages a collection of books.

    def __init__(self):
        self._books = []  # private list

    def add_book(self, book):
        # Add a new Book object to the library's collection.
        self._books.append(book)

    def check_out_book(self, title):
        # Check out a book by title.
        # If found and available → mark it checked out.
        
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        # Return a book by title.
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        # Print all books that are not checked out.
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
