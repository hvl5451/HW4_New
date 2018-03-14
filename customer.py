"""

Customer objects are created with attributes from Person, and have the option to create user accounts
and login to access more methods, such as change password, open account
deposit, withdraw, and check balance.

"""


from person import Person
from checking_account import CheckingAccount
from savings_account import SavingsAccount
import threading
import random
import datetime

class Customer(Person):

    """
    
    Implementation of a customer.
    Can create a user_account within the bank system.
    Can login, logout, and change password.
    Can request opening or closing an account.
    Can withdraw and deposit money, check balance of the customer's different accounts.

    """
    
    def __init__(self, name, birthdate, phone_number, \
                 password, customer_number):
        
        self.___password = password
        self._customer_number = random.randint(1000000000,10000000000)
        self.__customer_account_list = {}
        
        super().__init__(name, birthdate, phone_number)


        
    def set_password(self, newpass):
        """setter method for password; changes private attribute password to argument passed to it"""
        self.__password = newpass


    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone

    def set_name(self, temppass, newname):
        
        self._name = newname


    def set_phone_number(self, temppass, new_phone_number):
        self._phone_number = new_phone_number


    def create_account(self, account_type):
        
        if account_type.lower() == "checking":
            new_account = CheckingAccount (self.___name, str(datetime.datetime.now()), random.randint(1000000,10000000), account_type)
            
        if account_type.lower() == "saving":
            new_account = SavingsAccount (self.___name, str(datetime.datetime.now()), random.randint(1000000,10000000), account_type)

            
        self._customer_account_list[new_account.get_account_number()] = new_account
        self._customer_account_list[new_account.get_account_number()] = new_account

        
        print("account number is {}".format(new_account.get_account_number()))
        return new_account.get_account_number()
            

    def check_balance(self, account_number):
        return self._customer_account_list[account_number].get_balance()

    def withdraw(self, account_number, amount):
        self._customer_account_list[account_number].update_balance(amount*-1)
        print(" withdrew ${}", amount)


    def deposit(self, account_number, amount):
        self._customer_account_list[account_number].update_balance(amount)
        print(" withdrew ${}", amount)        
        
        
    def __str__(self):
        return "{},{}".format(self._name, self._customer_number)

    __repr__=__str__
    
    
