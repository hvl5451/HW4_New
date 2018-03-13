from employee import Employee

class Manager(Employee):
    def __init__(self, name, birthdate, phone_no, password):
        super().__init__(name, birthdate, phone_no, password)
