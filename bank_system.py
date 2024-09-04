import datetime
from typing import List, Dict
import hashlib
import re

class Customer:
    def __init__(self, customer_id: int, name: str, email: str, password_hash:str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.is_verified = False

class Account:
    def __init__(self, account_id: int, customer: Customer, balance: float = 0.0):
        self.account_id = account_id
        self.customer = customer
        self.balance = balance
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: 'Transaction'):
        self.transactions.append(transaction)
        self.balance += transaction.amount
        
    def last_transaction(self) -> 'Transaction':
        return self.transactions.pop() if self.transactions else None
    
class Transaction:
    def __init__(self, transaction_id: int, account: Account, amount: float, description: str):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.description = description
        self.timestamp = datetime.datetime.now()

class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class AccountSystem:
    def __init__(self):
        self.customers: Dict[int, Customer] = {}
        self.accounts: Dict[int, Account] = {}
        self.products: Dict[int, Product] = {}
        self.transactions: Dict[int, Transaction] = {}
    
    def create_customer(self, name: str, email: str, password: str) -> Customer:
        if not self._is_valid_email(email):
            raise ValueError("Invalid email")
        
        customer_id = len(self.customers) + 1
        password_hash = self._hash_password(password)
        customer = Customer(customer_id, name, email, password_hash)
        self.customers[customer_id] = customer
        return customer

    def verify_customer(self, customer_id: int):
        customer = self.get_customer(customer_id)
        if customer:
            customer.is_verified = True

    def sign_in(self, email: str, password: str) -> Customer:
        for customer in self.customers.values():
            if customer.email == email and customer.password_hash == self._hash_password(password):
                return customer
        return None

    def create_account(self, customer: Customer) -> Account:
        if not customer.is_verified:
            raise ValueError("Customer must be verified to create account")
        
        account_id = len(self.accounts) + 1
        account = Account(account_id, customer)
        self.accounts[account_id] = account
        return account

    def create_transaction(self, account: Account, amount: float, description: str) -> Transaction:
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, account, amount, description)
        self.transactions[transaction_id] = transaction
        account.add_transaction(transaction=transaction)
        return transaction

    def get_customer(self, customer_id: int) -> Customer:
        return self.customers.get(customer_id)

    def get_account(self, account_id: int) -> Account:
        return self.accounts.get(account_id)

    def get_last_transaction(self, account_id: int) -> Transaction:
        account = self.get_account(account_id)
        return account.last_transaction() if account else None

    def add_product(self, name: str, price: float, stock: int) -> Product:
        product_id = len(self.products) + 1
        product = Product(product_id, name, price, stock)
        self.products[product_id] = product
        return product

    def buy_product(self, account_id: int, product_id: int, quantity: int) -> bool:
        account = self.get_account(account_id)
        product = self.products.get(product_id)
        
        if not product or not account:
            return False

        cost = quantity * product.price
        if account.balance < cost or product.stock < quantity:
            return False
        
        self.create_transaction(account, -cost, f"Bought {quantity} of {product.name}")
        product.stock -= quantity
        return True

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return email_regex.match(email) is not None


system = AccountSystem()

# Create a customer
customer = system.create_customer("John Doe", "john@example.com", "password123")
system.verify_customer(customer.customer_id)

# Sign in
signed_in_customer = system.sign_in("john@example.com", "password123")
if signed_in_customer:
    print(f"Signed in as: {signed_in_customer.name}")

# Create an account for the customer
account = system.create_account(customer)

# Add some initial balance
system.create_transaction(account, 1000.0, "Initial deposit")

# Add a product
product = system.add_product("Laptop", 800.0, 10)

# Buy a product
if system.buy_product(account.account_id, product.product_id, 1):
    print("Purchase successful")
else:
    print("Purchase failed")

# Check account balance
print(f"Account balance: {account.balance}")

# Get the last transaction
last_transaction = system.get_last_transaction(account.account_id)
if last_transaction:
    print(f"Last transaction: {last_transaction.description}, Amount: {last_transaction.amount}")
else:
    print("No transactions found")
