from user import User


class Library:
    """A class representing a library that manages books and users."""
    libraries = []

    def __init__(self, library_name):
        """Initializes a new library with a given name.

        Args:
            library_name (str): The name of the library.
        """
        self.library_name = library_name
        self.books = {}
        self._users = {}
        self.__borrowed_books = {}

        Library.libraries.append(self)

    def register_user(self, user):
        """Registers a new user with the library.

        Args:
            user (User): The user to register with the library.

        Raises:
            TypeError: If the provided user is not an instance of User.
        """
        if not isinstance(user, User):
            raise TypeError("We can only register real users")

        user_id = user.get_user_id()

        self._users[user_id] = user

    def add_book(self, book, amount_copies=0, user_id=''):
        """Adds a book to the library's inventory or returns a borrowed book.

        Args:
            book: The book to add to the library's inventory.
            amount_copies (int, optional): The number of copies to add. Defaults to 0.
            user_id (str, optional): The ID of the user returning the book, if applicable.

        Raises:
            ValueError: If the user is returning a book that was not borrowed.
        """
        book_isbn = book.get_isbn()

        if user_id in self.__borrowed_books and book_isbn in self.__borrowed_books[user_id]:
            self.__borrowed_books[user_id].remove(book_isbn)

            if len(self.__borrowed_books[user_id]) == 0:
                del self.__borrowed_books[user_id]

        if book_isbn in self.books:
            self.books[book_isbn]['amount'] += 1
        else:
            self.books[book_isbn] = {'amount': amount_copies, 'book': book}

    def get_specific_book(self, book, user):
        """Allows a user to borrow a specific book from the library.

        Args:
            book: The book the user wants to borrow.
            user (User): The user who wants to borrow the book.

        Raises:
            ValueError: If the book is not available in the library or the user is not registered.

        Returns:
            bool: True if the book was successfully borrowed.
        """
        user_id = user.get_user_id()
        book_id = book.get_isbn()

        if self.books[book_id]['amount'] < 1:
            raise ValueError('No such book')

        if user_id not in self._users:
            raise ValueError('Before you can take a book, you must register with us')

        self.books[book_id]['amount'] -= 1
        self.__borrowed_books[user_id] = [book_id]
        user.add_borrowed_book(self, book)
        return True

    def delete_book(self, book_id):
        """Deletes a book from the library's inventory.

        Args:
            book_id (str): The ISBN of the book to delete.

        Raises:
            ValueError: If the book does not exist in the library
                        or if the book is borrowed by a user.
        """
        if book_id not in self.books:
            raise ValueError("We cannot delete a book that doesn't exist")

        for _, books in self.__borrowed_books.items():
            if book_id in books:
                raise ValueError('We cannot remove books until the user returns them')

        del self.books[book_id]

    def get_all_available_books(self):
        """Returns all available books in the library.

        Returns:
            dict: A dictionary containing all available books and their details in the library.
        """
        return self.books

    @classmethod
    def get_all_libraries(cls):
        """Returns a list of all libraries.

        Returns:
            list: A list of all Library instances.
        """
        return cls.libraries
