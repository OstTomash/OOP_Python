import re

from library import Library


class Book:
    """A class representing a book.

    A book has a title, an author, an ISBN, and a certain number of copies.
    """
    def __init__(self, title, author, isbn, copies):
        """Initializes a book with a title, author, ISBN, and number of copies.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            copies (int): The number of copies of the book.

        Raises:
            ValueError: If the ISBN is not in the correct format.
        """
        self.title = title
        self.author = author
        self._isbn = self.validate_isbn(isbn)
        self.copies = copies

    def check_availability(self):
        """Checks the availability of the book in all libraries.

        Returns:
            str: Information about the book's availability in each library.
        """
        libraries = Library.get_all_libraries()

        for library in libraries:
            if not library.books[self._isbn]:
                return f"{library.library_name}: Not available"

            return (f'This book is available in {library.library_name}'
                    f'in quantity {library.books[self._isbn]['amount']}')

    def update_copies_in_library(self, amount=1):
        """Updates the number of copies of the book in the library.

        Args:
            amount (int, optional): The amount by which to decrease the copies. Defaults to 1.
        """
        self.copies -= amount

    def get_book_info(self, attribute=''):
        """Returns information about the book.

        Args:
            attribute (str, optional): The specific attribute to retrieve information about.
                                       Defaults to ''.

        Returns:
            str: Information about the book's attribute,
                 or the title and author if attribute is not specified.
        """
        if attribute == '':
            return f'{self.title} - {self.author}'

        return getattr(self, attribute, 'No such attribute')

    def get_isbn(self):
        """Returns the ISBN of the book.

        Returns:
            str: The ISBN of the book.
        """
        return self._isbn

    @staticmethod
    def validate_isbn(isbn):
        """Validates the ISBN of the book.

        Args:
            isbn (str): The ISBN to validate.

        Raises:
            ValueError: If the ISBN is not in the correct format.

        Returns:
            str: The validated ISBN.
        """
        pattern = re.compile(r'^\d-\d{3}-\d{5}-\d$')

        if not pattern.match(isbn):
            raise ValueError('ISBN is not correct')

        return isbn
