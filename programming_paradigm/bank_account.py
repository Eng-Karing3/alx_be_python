class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The initial balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = float(initial_balance) # Ensure internal balance is a float

    # Removed _format_transaction_amount helper.
    # All currency amounts will now be formatted with 2 decimal places.

    def deposit(self, amount):
        """
        Deposits the specified amount to the account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        # Format to two decimal places, e.g., 50 -> 50.00
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            # Format to two decimal places, e.g., 20 -> 20.00
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            # This specific string does not involve an amount, so it's already exact.
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        # Always format to two decimal places, e.g., 100 -> 100.00
        print(f"Current Balance: ${self.__account_balance:.2f}")
