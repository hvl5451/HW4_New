from person import Person
from random import randint
from customer import Customer
class Employee(Person):
    eid_list=[] #getter method should be added to the bank
    def __init__(self, name, birthdate, phone_no):
        super().__init__(name, birthdate, phone_no)
        self._eid=randint(10000, 99999)
        Employee.eid_list.append(self._eid)
        print("Welcome {}, your ID is:{}".format(self._name, self._eid))
        
    def get_eid(self):
        return self._eid
    
    def display_customer_details(self, c):
        return "Name:{}".format(c._name)
        return "Phone Number:{}".format(c.phone_no())
        return "Account no:{}".format(c.get_customer_no())
        return "Balance:{}".format(c.get_balance()))

    def edit_customer_details(self, c):
        raise NotImplementedError("Can be accessed by only Manager")

    def remove_customer(self, c):
        raise NotImplementedError("Can be accessed by only Manager")
