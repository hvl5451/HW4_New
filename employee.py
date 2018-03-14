"""
Employee objects are created with attributes from Person, and have the option to
generate a random employee id and password.
It has methods that allows to display customer details and employee id.
An Employee has a Manager and a Teller
"""
from person import Person
from random import randint
from customer import Customer
class Employee(Person):
    """
    Implementation of Employee
    Can generate a employee id
    Can Stores the details of the Employee
    Can Display customer details

    """
    eid_list=[] #getter method should be added to the bank
    def __init__(self, name, birthdate, phone_no):
        super().__init__(name, birthdate, phone_no)
        self._eid=randint(10000, 99999)
        Employee.eid_list.append(self._eid)
        print("Welcome {}, your ID is:{}".format(self._name, self._eid))


    def get_eid(self):
        """Returns the Employee ID"""
        return self._eid

    def display_customer_details(self, c):
        """Displays Customer details like Name, Phone Number, Account number, amd Balance"""
        return "Name:{}".format(c._name)
        return "Phone Number:{}".format(c.phone_no())
        return "Account no:{}".format(c.get_customer_no())
        return "Balance:{}".format(c.get_balance())

    def edit_customer_details(self, c):
        """Raises Error because this function can be accessed """
        raise NotImplementedError("Can be accessed by only Manager")

    def remove_customer(self, c):
        """Raises Error becasue this function can be accessed"""
        raise NotImplementedError("Can be accessed by only Manager")
