#!/usr/bin/python3
"""
Checkbook program that allows deposits, withdrawals, and balance inquiries.
"""

class Checkbook:
    """
    Class representing a simple checkbook with deposit, withdraw, and balance methods.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the checkbook via command-line input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            print("Exiting checkbook program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()