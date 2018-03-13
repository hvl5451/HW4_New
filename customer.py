"""

Customer objects are created with attributes from Person, and have the option to create user accounts
and login to access more methods, such as change password, request account open, request account close,
deposit, withdraw, check balance, etc. Customers cannot open or close accounts by themselves, but have
methods to request these actions which should be approved by the manager.

"""


from person import Person
from account import Account
import threading
import random

class Customer(Person):

    """
    
    Implementation of a customer.
    Can create a user_account within the bank system.
    Can login, logout, and change password.
    Can request opening or closing an account.
    Can withdraw and deposit money, check balance of the customer's different accounts.

    """
    
    def __init__(self, name, birthdate, phone_number, \
                 password = None, customer_number = None, Login = False):
        self.__password = password
        self._Login = Login
        
        super().__init__(name, gender, birthdate, phone_number)

    """
    
    Login property that can be true and false for each instance of customer depending if
    they login with their user account number and password. When this property is false,
    certain methods are disabled

    """

    @property
    def Login(self):
        
        """getter method for Login property"""
        
        return self._Login

    @Login.setter
    def Login(self,value):
        
        """ setter method for Login property """
        
        self._Login = value

    def create_usraccount(self, password, birthdate):
        if birthdate != self.birthdate:
            raise ValueError("birthdates do not match. Security verification failed")
        else:
            self.__password = password
            self.customer_number = random.randint(1000000000,10000000000)
            print("account number is {}".format(self.customer_number))

    def login(self, act_num, temp_pass):
        if temp_pass != self.__password or act_num != self.customer_number:
            raise Exception("invalid password or account number")
        else:
            self._Login = True
            threading.Timer(900.0, self.logout).start()
            print("logged in")

    def logout(self):
        self.Login = False
        print("logged out")
            
        
    def change_password(self, oldpass, newpass):
        if self.Login == False:
            raise Exception("not logged in")
        elif oldpass != self.__password:
            raise ValueError("previous password invalid")
        else:
            self.__password = newpass
        
    def __str__(self):
        return "{},{}".format(self.name, self.customer_number)

    __repr__=__str__
    
    def create_bankaccount(self):
        return 0
