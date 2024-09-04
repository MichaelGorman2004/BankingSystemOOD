# Customer Account System

## Overview

This Customer Account System is a Python-based backend simulation for managing customer accounts, transactions, and product purchases. It provides a foundation for building e-commerce platforms or banking systems.

## Features

- Customer Management
  - Create and verify customer accounts
  - Secure password hashing
  - Customer sign-in functionality

- Account Management
  - Create accounts for verified customers
  - Track account balances
  - Record and retrieve transactions

- Product Management
  - Add products to the system
  - Track product inventory

- Transaction Handling
  - Process deposits and withdrawals
  - Handle product purchases
  - Maintain transaction history

## Requirements

- Python 3.6+

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/customer-account-system.git
   ```
2. Navigate to the project directory:
   ```
   cd customer-account-system
   ```

## Usage

To run the example script:

```
python bank_system.py
```

This will execute a series of operations demonstrating the system's functionality, including:
- Creating a customer
- Signing in
- Creating an account
- Adding funds
- Adding a product
- Purchasing a product

## Code Structure

- `Customer`: Represents a customer with basic information and verification status
- `Account`: Manages account details and transactions
- `Transaction`: Represents individual financial transactions
- `Product`: Represents items available for purchase
- `AccountSystem`: Orchestrates interactions between other classes

## Example

```python
system = AccountSystem()

# Create and verify a customer
customer = system.create_customer("John Doe", "john@example.com", "password123")
system.verify_customer(customer.customer_id)

# Sign in
signed_in_customer = system.sign_in("john@example.com", "password123")

# Create an account and add funds
account = system.create_account(customer)
system.create_transaction(account, 1000.0, "Initial deposit")

# Add a product and make a purchase
product = system.add_product("Laptop", 800.0, 10)
system.buy_product(account.account_id, product.product_id, 1)

# Check balance and last transaction
print(f"Account balance: {account.balance}")
last_transaction = system.get_last_transaction(account.account_id)
print(f"Last transaction: {last_transaction.description}, Amount: {last_transaction.amount}")
```

## Future Enhancements

- Database integration for persistent storage
- User interface (web or mobile app)
- More robust error handling and logging
- Integration with external payment systems
- Implementation of a recommendation system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
