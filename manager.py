
"""
Manager is inherited from Employee and has the option to edit the customer details.
Manager has the option to edit customer details like name, birthdate, phone number.
Manager can create account for customer and remove customer's account
"""
import datetime
from employee import Employee
from customer import Customer
from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from random import randint
class Manager(Employee):

    """Implementation of a Manager
        Can edit customer name
        Can edit customer birthdate
        can edit phone number
        can create account for customer
        can remove account for customer
    """
    def __init__(self, name, birthdate, phone_no):
        super().__init__(name, birthdate, phone_no)

    def edit_customer_name(self, c, name):
        """calls the set_name() function from Customer to edit customer name"""
        c.set_name(name)

    def edit_customer_birthdate(self, c, birthdate):
        """calls the set_birthdate() from Customer to edit Customer birthdate"""
        c.set_birthdate(birthdate)

    def edit_phone_no(self, c, phone_no):
        """calls the set_phone_no() from Customer to edit Customer Phone number"""
        c.set_phone_no(phone_no)

    def create_account_for_customer(self, c, account_type):
        """creates a new account for customer"""
        account_num = randint(1, 100000000);
        if account_type == "Savings":
            new_account = SavingsAccount(c.get_name(),datetime.date.today().ctime(),\
            account_num, account_type)
        elif account_type == "Checking":
            new_account = CheckingAccount(c.get_name(),datetime.date.today().ctime(),\
            account_num, account_type)

        c.add_account(new_account)

    def remove_account_for_customer(self, c, account_number):
        """deletes a customer's account"""
        del c.get_accounts()[account_number]
