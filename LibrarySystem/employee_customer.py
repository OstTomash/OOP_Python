from user import User
from book import Book


class Employee(User):
    """A class representing a library employee who is also a user.

    An employee can manage books in the library and has a salary.
    """
    def __init__(self, name, salary, library):
        """Initializes an employee with a given name, salary, and library.

        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee.
            library (Library): The library where the employee works.
        """
        super().__init__(name)
        self.__salary = salary
        self.library = library

    def get_information(self):
        """Returns information about the employee.

        Returns:
            str: A formatted string containing the employee's name, place of work, and salary.
        """
        return (f'Name: {self.name}\n'
                f'Works at {self.library.get_library_name()}\n'
                f'Salary: {self.__salary}')

    def add_book(self, book, amount_copies):
        """Adds a book to the library's inventory.

        Args:
            book (Book): The book to be added to the library's inventory.
            amount_copies (int): The number of copies of the book to add.

        Raises:
            ValueError: If the provided book is not an instance of the Book class.
            ValueError: If the amount of copies to add is less than or equal to zero.
            ValueError: If trying to add more copies than available.
        """
        if not isinstance(book, Book):
            raise ValueError("It`s not a book")

        if amount_copies <= 0:
            raise ValueError("You should add at least one book")

        if amount_copies > book.get_amount_copies():
            raise ValueError("You cannot add more books than there are copies.")

        user_id = self.get_user_id()
        self.library.add_book(book, amount_copies, user_id)
        book.update_copies_in_library(amount_copies)

    def remove_book(self, book_id):
        """Removes a book from the library's inventory.

        Args:
            book_id (str): The ID of the book to be removed.

        Raises:
            ValueError: If the book does not exist in the library's inventory.
        """
        self.library.delete_book(book_id)


class Customer(User):
    """A class representing a library customer who is also a user.

    Customers can borrow books from the library.
    """
