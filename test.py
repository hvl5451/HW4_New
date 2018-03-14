from customer import Customer
from random import randint
from manager import Manager
c = Customer("J", "1/1/1", "2112121", randint(10, 100000))
m = Manager("J", "1/1/1", "2112121")
m.create_account_for_customer(c, "savings")

print (c._customer_account_list.keys())
