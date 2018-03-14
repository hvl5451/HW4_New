"""
Accounts are accessible by customers and every employee.
Account information can be modified only by customers and managers.
Accounts can only be closed/deleted by managers.
"""

import datetime
class Account:
    """
    Implementation of a customer's bank account.
    Can hold and update a balance.
    Can process withdrawals and deposits made by the account holder.
    """
    def __init__(self, holder, created_on, account_number, account_type, balance=0.0):
        self._holder = holder
        self._created_on = created_on
        self._account_number = account_number
        self._account_type = account_type
        self._balance = balance

    def get_holder(self):
        """Returns the customer that holds the account."""
        return self._holder

    def get_created_on(self):
        """Returns the date the account was created on."""
        return self._created_on

    def get_account_number(self):
        """Returns the unique identification number of the account."""
        return self._account_number

    def get_account_type(self):
        """Gets the type of the account (savings, checking, etc.)"""
        return self._account_type

    def get_balance(self):
        """Returns the amount of money in the account."""
        return self._balance

    def update_balance(self, amount):
        """
        Raises or lowers the balance in the account.

        Args:
            amount - quantity of money to be added to / removed from
            the account balance
        """
        self._balance += amount
