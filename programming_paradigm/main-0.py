import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line interactions with BankAccount.
    """
    account = BankAccount(100.00)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command-line argument into command and optional amount
    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()  # Convert command to lowercase for case-insensitivity
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except ValueError:
        print("Error: Amount must be a valid number.")
        sys.exit(1)
    except IndexError:
        # This handles cases like 'display' where no amount is expected
        command = sys.argv[1].lower()
        amount = None


    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            account.withdraw(amount)
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display" and amount is None:
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()