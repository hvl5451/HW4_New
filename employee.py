from person import Person
from random import randint

class Employee(Person):
    eid_list=[] #getter method should be added to the bank
    def __init__(self, name, birthdate, phone_no, password):
        super().__init__(name, birthdate, phone_no)
        self.__password=password
        self._eid=randint(10000, 99999)
        Employee.eid_list.append(self._eid)
        print("Welcome {}, your ID is:{}".format(self._name, self._eid))

    @classmethod
    def list_getter(cls):
        return Employee.emp_list

    def get_eid(self):
        return self._eid

    def display_customer_details(self, obj):
        'display customer details, return getter functions of customer'

    def edit_customer_details(self, obj):
        raise NotImplementedError("Can be accessed by only Manager")

    def remove_customer(self, obj):
        raise NotImplementedError("Can be accessed by only Manager")









