"""
Teller inherits from Employee
The important function of the teller would display the customer details which is obtained from employee class
"""

from employee import Employee

class Teller(Employee):
    def __init__(self, name, birthdate, eid, phone_no):
        super().__init__(name, birthdate, eid, phone_no)
