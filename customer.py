"""

Customer objects are created with attributes from Person, and have the option to create user accounts
and login to access more methods, such as change password, open account
deposit, withdraw, and check balance.

"""


from person import Person
from checking_account import CheckingAccount
from savings_account import SavingsAccount
import random
import datetime

class Customer(Person):

    """

    Implementation of a customer.
    Can create a user_account within the bank system.
    Can request opening or closing an account.
    Can withdraw and deposit money, check balance of the customer's different accounts.
    Upon creation, the randomly generated customer number will be printed.

    """

    def __init__(self, name, birthdate, phone_number, \
                 customer_number):


        super().__init__(name, birthdate, phone_number)
        self._customer_number = random.randint(1000000000,10000000000)
        self.__customer_account_list = {}

        print("account number is {}".format(self._customer_number))




    def get_name(self):
        """
        getter method for name
        returns the protected attribute name
        """
        return self._name

    def get_phone_number(self):
        """
        getter method for phone_number
        returns the protected attribute phone_number
        """
        return self._phone

    def set_name(self, newname):
        """
        setter method for name
        changes protected attribute name to argument passed to it
        """
        self._name = newname


        self._customer_number = random.randint(1000000000,10000000000)
        self._customer_account_list = {}

        super().__init__(name, birthdate, phone_number)

    def create_account(self, account_type):

        """
        method for creating bank account objects
        constructs instances of the Account subclasses with customer attributes:
            -customer name
            -time of method call
            -a random 7-digit integer
            -type of account; a method argument, determines which subclass of Account is created

        returns the account number and prints a message containing the account number
        """



        if account_type.lower() == "checking":
            new_account = CheckingAccount (self._name, str(datetime.datetime.now()), random.randint(1000000,10000000), account_type, balance=0.0)

        if account_type.lower() == "savings":
            new_account = SavingsAccount (self._name, str(datetime.datetime.now()),random.randint(1000000,10000000), account_type, balance=0.0)
            print ("account # is {}".format(new_account.get_account_number()))

        self._customer_account_list[new_account.get_account_number()] = new_account
        #self._customer_account_list[new_account.get_account_number()] = new_account


        print("account number is {}".format(new_account.get_account_number()))
        return new_account.get_account_number()


    def check_balance(self, account_number):
        """
        getter method for balance
        returns the balance attribute of the specific account object from the dictionary
        of the customer's accounts
        """

        return self._customer_account_list[account_number].get_balance()

    def withdraw(self, account_number, amount):
        """
        method for simulating withdrawing money
        will reduce the targeted account's balance based on the amount given in the argument
        uses the Account update_balance method which modifies the balance
        """

        self._customer_account_list[account_number].update_balance(amount*-1)
        print(" withdrew ${}", amount)


    def deposit(self, account_number, amount):
        """
        method for simulating withdrawing money
        will reduce the targeted account's balance based on the amount give nin the argument
        uses the Account update_balance method which modifiies the balance
        """

        self._customer_account_list[account_number].update_balance(amount)
        print(" withdrew ${}", amount)


    def __str__(self):
        """
        overwriting the str method; will show the name nad customer number if customer object is printed or represented
        """
        return "{},{}".format(self._name, self._customer_number)

    __repr__=__str__
