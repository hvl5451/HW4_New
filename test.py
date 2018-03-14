import datetime
from random import randint
from employee import Employee
from customer import Customer
from person import Person
from account import Account

c = Customer("Jon", "01/01/17", "2151212121", randint(1, 100000))
print (c.get_name())
c.create_account("checking")

m = Manager()
