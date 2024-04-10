from abc import ABC, abstractmethod
import uuid


class BankAccount(ABC):
    """Abstract base class representing a bank account.

    Attributes:
        _balance (float): The current balance of the bank account.
        _owner (str): The owner of the bank account.
        _account_number (str): The unique account number of the bank account.

    Methods:
        withdraw(amount): Abstract method to withdraw funds from the account.
        deposit(amount): Abstract method to deposit funds into the account.
        get_balance(): Returns the current balance of the account.
        get_account_number(): Returns the account number of the account.
        generate_account_number(): Static method to generate a unique account number.
    """
    def __init__(self, owner):
        """Initialize a BankAccount object.

        Args:
            owner (str): The owner of the bank account.
        """
        self._balance = 0
        self._owner = owner
        self._account_number = self.generate_account_number()

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method to withdraw funds from the account."""
        pass

    @abstractmethod
    def deposit(self, amount):
        """Abstract method to deposit funds into the account."""
        pass

    def get_balance(self):
        """Return the current balance of the account."""
        return self._balance

    def get_account_number(self):
        """Return the account number of the account."""
        return self._account_number

    @staticmethod
    def generate_account_number():
        """Generate a unique account number."""
        return str(uuid.uuid4().hex)[:10]
