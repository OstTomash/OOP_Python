class Customer:
    """Class representing a customer.

    Attributes:
        name (str): The name of the customer.
        email (str): The email address of the customer.
        _customer_id (str): The unique identifier of the customer.

    Methods:
        get_information(): Returns a formatted string containing customer information.
    """
    def __init__(self, name, email, customer_id):
        """Initialize a Customer object.

        Args:
            name (str): The name of the customer.
            email (str): The email address of the customer.
            customer_id (str): The unique identifier of the customer.
        """
        self.name = name
        self.email = email
        self._customer_id = customer_id

    def get_information(self):
        """Return formatted customer information."""
        return f"Name: {self.name}\nEmail: {self.email}\nCustomer ID: {self._customer_id}\n"
