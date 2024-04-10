from customer import Customer
from savings_account import SavingsAccount

customer = Customer("Ostap Tomash", "ostapTomash@gmail.com", "123456")
customer_account = SavingsAccount(customer)

print(customer.get_information())
print("Account Number:", customer_account.get_account_number())

customer_account.deposit(1000)
print("Balance:", customer_account.get_balance())

customer_account.withdraw(500)
print("Balance:", customer_account.get_balance())