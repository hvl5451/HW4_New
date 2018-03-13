import datetime

class Person:

    def __init__(self, name, birthdate, phone_no):
        self._name=name
        self._birthday=birthdate
        self._phone_no=phone_no

    def get_name(self):
        return self._name

    def get_birthdate(self):
        return self._birthday

    def get_phone_no(self):
        return self._phone_no

    def get_age(self):
        today = datetime.date.today()
        month, day, year = self._birthday.split("/")
        age = today.year - int(year)
        if (today.month, today.day) < (int(month), int(day)):
            age -= 1
        return age



