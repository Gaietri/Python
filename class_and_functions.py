# functions
import logging

logging.log(1, "hello")

def add_numbers(a, b=1):
    return a + b


result = add_numbers(a=1, b=3)


# sachin = print(result)


# Class
class Customer:
    def __init__(self, name, customer_id, dob):
        self.name = name
        self.customer_id = customer_id
        self.balance = 0
        self.is_kyc_done = False
        self.products = []
        self.dob = dob
        self.address = None
        self.marital_status = None
        self.tax_residency = None

    def get_balance(self):
        return self.balance

    def credit(self, amount):
        self.balance = self.balance + amount

    def debit(self, amount):
        self.balance = self.balance - amount


customer1 = Customer("Sachin", 1234, "17/10/89")
customer2 = Customer("gayatri", 1235, "17/11/89")
# customer1 = Customer()
# customer2 = Customer()
# customer2.balance = 1
# customer1.balance = 0
# customer1.name = "sachin"
print(customer1.get_balance())
customer1.credit(10000)
customer2.debit(-500004000)
print(customer1.get_balance())
print(customer2.get_balance())
