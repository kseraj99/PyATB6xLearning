
class Bank:

    def __init__(self, account_number, balance):
        # Private attribute to store account number
        # Private means it cannot be accessed outside the class using object.__account
        self.__account = account_number

        # Public attribute for balance
        self.bala = balance

    def check_balance(self):
        """Print the current balance"""
        print("Current Balance:", self.bala)

    def deposit(self, amount):
        """Add money to the account balance"""
        self.bala = self.bala + amount
        print(f"Deposited: {amount}")

    def show_me_account_number(self, is_auth):
        """
        Print the account number only if the user is authenticated.
        is_auth: True or False
        """
        if is_auth:
            print("Account Number:", self.__account)
        else:
            print("Not Allowed: Authentication Failed")


# Creating an object of Bank class
axis = Bank(1919191919, 100)

# Deposit 100 rupees
axis.deposit(100)

# Check updated balance
axis.check_balance()

# Show account number (allowed because authentication is True)
axis.show_me_account_number(True)
