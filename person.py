"""
Person is the super class of this whole implementation.
A Person can be a specific employee or a customer.
"""


import datetime

class Person:
    """
    Implementation of Person Class
    intializes name, birthdate, phone number of person

    """

    def __init__(self, name, birthdate, phone_no):
        self._name=name
        self._birthday=birthdate
        self._phone_no=phone_no

    def get_name(self):
        """Returns the name of the Person"""
        return self._name

    def get_birthdate(self):
        """Returns the birthdate of the Person"""
        return self._birthday

    def get_phone_no(self):
        """Returns the phone number of the Person"""
        return self._phone_no

    def get_age(self):
        """Calculates the age of the person from the birthdate and returns the age"""
        today = datetime.date.today()
        month, day, year = self._birthday.split("/")
        age = today.year - int(year)
        if (today.month, today.day) < (int(month), int(day)):
            age -= 1
        return age


