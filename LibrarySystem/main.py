import json

from library import Library
from book import Book
from employee_customer import Employee, Customer

with open('mocked_books.json') as json_file:
    mocked_books = json.load(json_file)

first_library = Library('First library')
second_library = Library('Second library')
third_library = Library('Third library')

first_employee = Employee('Brad Pit', 1500, first_library)
second_employee = Employee('John Down', 2000, second_library)
third_employee = Employee('John Up', 2500, third_library)

first_customer = Customer('Joe Pit')

first_book = Book(**mocked_books[0])
second_book = Book(**mocked_books[1])
third_book = Book(**mocked_books[2])

first_employee.add_book(first_book, 8)
print(first_book.check_availability())
first_library.register_user(first_customer)
first_library.get_specific_book(first_book, first_customer)
first_customer.return_book(first_book, first_library)
first_employee.remove_book(first_book.get_isbn())
print(first_customer.get_information())

first_available_books = first_library.get_all_available_books()
print(first_available_books)
