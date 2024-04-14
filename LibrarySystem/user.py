import uuid
from abstract_person import Person


class User(Person):
    """A class representing a library user. Inherits from the Person class."""
    def __init__(self, name):
        """Initializes a new user with a given name.

        Args:
            name (str): The name of the user.
        """
        self.name = name
        self._borrowed_books = {}
        self.__user_id = self.generate_user_id()

    def get_information(self):
        """Returns information about the user.

        Returns:
            str: A string containing the user's name and a list of borrowed books.
        """
        return f'Name: {self.name}, Borrowed books: {self._borrowed_books}'

    def take_book(self, book, library):
        """The user borrows a book from the library.

        Args:
            book: The book the user wants to borrow.
            library: The library from which the user borrows the book.
        """
        book_isbn = book.get_isbn()

        if library.get_specific_book(book, self):
            self._borrowed_books[library.library_name] = book_isbn

    def return_book(self, book, library):
        """The user returns a book to the library.

        Args:
            book: The book the user wants to return.
            library: The library to which the user returns the book.
        """
        library.add_book(book, user_id=self.__user_id)
        should_remove = False

        for library_name in self._borrowed_books.items():
            if (
                    library_name == library.library_name and
                    self._borrowed_books[library_name] == book.get_isbn()
            ):
                should_remove = True

        if should_remove:
            del self._borrowed_books[library.library_name]

    def add_borrowed_book(self, library, book):
        """Adds a borrowed book to the user's borrowed books list.

        Args:
            library: The library from which the book was borrowed.
            book: The book that was borrowed.
        """
        self._borrowed_books[library.library_name] = book.get_isbn()

    def get_user_id(self):
        """Returns the user's unique ID.

        Returns:
            str: The user's unique ID.
        """
        return self.__user_id

    @staticmethod
    def generate_user_id():
        """Generates a unique user ID.

        Returns:
            str: A unique 10-character user ID.
        """
        return str(uuid.uuid4().hex)[:10]
