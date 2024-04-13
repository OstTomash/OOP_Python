from abc import ABC, abstractmethod


class Person(ABC):
    """An abstract base class representing a person.

    This class defines the interface for a person who interacts with a library,
    including methods for obtaining information, borrowing books, and returning books.
    """
    @abstractmethod
    def get_information(self):
        """Returns information about the person.

        This method should be implemented by subclasses to provide
        specific information about the person.

        Returns:
            str: Information about the person.
        """

    @abstractmethod
    def take_book(self, book, library):
        """Allows the person to take a book from the library.

        This method should be implemented by subclasses to handle
        the process of borrowing a book from a library.

        Args:
            book: The book to be taken from the library.
            library: The library from which the book is to be taken.

        Returns:
            None
        """

    @abstractmethod
    def return_book(self, book, library):
        """Allows the person to return a book to the library.

        This method should be implemented by subclasses to handle
        the process of returning a book to a library.

        Args:
            book: The book to be returned to the library.
            library: The library to which the book is to be returned.

        Returns:
            None
        """
