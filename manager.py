
import datetime
from employee import Employee
from customer import Customer
from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from random import randint
class Manager(Employee):
    def __init__(self, name, birthdate, phone_no):
        super().__init__(name, birthdate, phone_no)

    def edit_customer_name(self, c, name):
        c.set_name(name)

    def edit_customer_birthdate(self, c, birthdate):
        c.set_birthdate(birthdate)

    def edit_phone_no(self, c, phone_no):
        c.set_phone_no(phone_no)

    def create_account_for_customer(self, c, account_type):
        account_num = randint(1, 100000000);
        if account_type == "Savings":
            new_account = SavingsAccount(c.get_name(),datetime.date.today().ctime(),\
            account_num, account_type)
        elif account_type == "Checking":
            new_account = CheckingAccount(c.get_name(),datetime.date.today().ctime(),\
            account_num, account_type)

        c.add_account(new_account)

    def remove_account_for_customer(self, c, account_number):
        del c.get_accounts()[account_number]
