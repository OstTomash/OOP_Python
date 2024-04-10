from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """Class representing a savings account.

    Attributes:
        Inherits attributes from BankAccount.

    Methods:
        deposit(amount): Deposit funds into the savings account.
        withdraw(amount): Withdraw funds from the savings account.
    """
    def __init__(self, owner):
        """Initialize a SavingsAccount object.

        Args:
            owner (str): The owner of the savings account.
        """
        super().__init__(owner)

    def deposit(self, amount):
        """Deposit funds into the savings account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If amount is less than zero.
        """
        if amount < 0:
            raise ValueError("Amount should be greater than zero.")

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw funds from the savings account.

         Args:
             amount (float): The amount to withdraw.

         Raises:
             ValueError: If amount is less than zero or if there are insufficient funds.
         """
        if amount < 0:
            raise ValueError("Amount should be greater than zero")
        elif self._balance < amount:
            raise ValueError("Insufficient funds")

        self._balance -= amount
