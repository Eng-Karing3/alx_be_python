import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100.00)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except ValueError:
        print("Error: Amount must be a valid number.")
        sys.exit(1)
    except IndexError:
        command = sys.argv[1].lower()
        amount = None

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
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
