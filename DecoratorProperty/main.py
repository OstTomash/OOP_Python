class Account:
    """
    A class representing a bank account.

    Attributes:
        __balance (float): The balance of the account (private attribute).
        _account_holder (str): The holder of the account (protected attribute).

    Methods:
        get_balance: Retrieves the balance of the account.
    """

    def __init__(self, balance, holder):
        """
        Initializes a new instance of Account.

        Parameters:
            balance (float): The initial balance of the account.
            holder (str): The name of the account holder.
        """
        self.__balance = balance
        self._account_holder = holder

    @property
    def balance(self):
        """
        Retrieves the balance of the account.

        Returns:
            float: The balance of the account.
        """
        return self.__balance

    @balance.setter
    def balance(self, value):
        """
        Sets the balance of the account.

        Parameters:
            value (float): The new balance to be set.

        Raises:
            ValueError: If the value is not positive.
        """
        if value <= 0:
            raise ValueError("Balance should be positive")
        self.__balance = value


account = Account(123.456789, 'Ostap')
account.balance = 24
print(account.balance)
