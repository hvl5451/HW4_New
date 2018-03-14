"""
Teller inherits from Employee
The important function of the teller would display the customer details which is obtained from employee class
"""

from employee import Employee

class Teller(Employee):
    def __init__(self, name, birthdate, phone_no, password):
        super().__init__(name, birthdate, phone_no,password)


