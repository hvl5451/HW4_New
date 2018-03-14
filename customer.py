"""

Customer objects are created with attributes from Person, and have the option to create user accounts
and login to access more methods, such as change password, open account
deposit, withdraw, and check balance.

"""


from person import Person
from account import Account
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
                 password = None, customer_number = None):
        self.__password = password
        self.__customer_account_list = {}
        
        super().__init__(name, birthdate, phone_number)

    """
    
    Login property that can be true and false for each instance of customer depending if
    they login with their user account number and password. When this property is false,
    certain methods are disabled

    """


    def create_usraccount(self, password, birthdate):
        if birthdate != self.birthdate:
            raise ValueError("birthdates do not match. Security verification failed")
        else:
            self.__password = password
            self.customer_number = random.randint(1000000000,10000000000)
            print("account number is {}".format(self.customer_number))


            
        
    def set_password(self, oldpass, newpass):
        self.__password = newpass


    def set_name(self, temppass, newname):
        self.name = newname


    def set_phone_number(self, temppass, new_phone_number):
        self.phone_number = new_phone_number


    def create_account(self, account_type):
        new_account = Account (self.name, str(datetime.datetime.now()), random.randint(1000000,10000000), account_type)
        self.__customer_account_list[new_account.get_account_number()] = new_account
        self.__customer_account_list[new_account.get_account_number()] = new_account
        print("account number is {}".format(new_account.get_account_number()))
        return new_account.get_account_number()
            

    def check_balance(self, account_number):
        return self.__customer_account_list[account_number].get_balance()

    def withdraw(self, account_number, amount):
        self.__customer_account_list[account_number].update_balance(amount*-1)
        print(" withdrew ${}", amount)


    def deposit(self, account_number, amount):
        self.__customer_account_list[account_number].update_balance(amount)
        print(" withdrew ${}", amount)        
        
        
    def __str__(self):
        return "{},{}".format(self.name, self.__customer_number)

    __repr__=__str__
    
    
