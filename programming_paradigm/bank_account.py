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

    def _format_currency(self, amount):
        """
        Helper method to format currency amounts.
        If the amount is a whole number (e.g., 50.0), it's formatted as an integer (e.g., "50").
        Otherwise (e.g., 12.5), it's formatted to two decimal places (e.g., "12.50").
        """
        if amount == int(amount):
            return str(int(amount))
        else:
            return f"{amount:.2f}"

    def deposit(self, amount):
        """
        Deposits the specified amount to the account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        print(f"Deposited: ${self._format_currency(amount)}")

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
            print(f"Withdrew: ${self._format_currency(amount)}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self._format_currency(self.__account_balance)}")
