"""
bank objects are created independently from the other classes, and are
designed to be a container for the other classes, i.e. by storing instance
variables of custoemr and employee in dictionaries. Bank objects also contain
the bank name and bank hours, which can be modified using methods.
"""

import datetime
from employee import Employee
from customer import Customer

class Bank:

    """
    Implementation of a bank.
    Can create a bank object that contains instances of customers and employees
    Can add and delete customers and employees from their respsective lists
    By containing employees and customers, it also contains their attributes and account objects
    Can print the open hours as well as tell if the bank is open based on current time
    """
    

    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__bank_openhours = {0: None, \
                               1: datetime.time(9,0), \
                               2: datetime.time(9,0), \
                               3: datetime.time(9,0), \
                               4: datetime.time(9,0), \
                               5: datetime.time(9,0), \
                               6: datetime.time(10,0)}

        self.__bank_closehours = {0: None, \
                               1: datetime.time(16,30), \
                               2: datetime.time(16,30), \
                               3: datetime.time(16,30), \
                               4: datetime.time(16,30), \
                               5: datetime.time(16,30), \
                               6: datetime.time(13,0)}

        self.__customer_list = {}
        self.__employee_list = {}
        
    
    def get_bankname(self):
        """
        getter method for bank_name
        returns the private attribute bank_name
        """
        return self.__bank_name
    
    def get_customer_list(self):
        """
        getter method for customer_list
        returns the private attribute customer_list
        """
        return self.__customer_list
    
    def get_employee_list(self):
        """
        getter method for employee_list
        returns the private attribute customer_list
        """
        return self.__employee_list
    
    
    def timeopen(self, day):
        """
        method that supplements the gethours method
        returns a time open and time close datetime values in a reader-friendly string
        converts the 24-hour format of datetime to 12-hour format with AM and PM
        """
        __noonopen="AM"
        __noonclose="AM"
        if self.__bank_openhours[day] == None and self.__bank_closehours[day] == None:
            return "closed"
        if self.__bank_openhours[day].hour > 12:
            __noonopen = "PM"
        if self.__bank_closehours[day].hour > 12:
            __noonclose = "PM"

        return "{}:{}{} to {}:{}{}".format(self.__bank_openhours[day].hour%12,\
                                           str((self.__bank_openhours[day].minute)%12).zfill(2), \
                                           __noonopen, \
                                           self.__bank_closehours[day].hour%12, \
                                           str((self.__bank_closehours[day].minute)%12).zfill(2), \
                                           __noonclose)

    def get_hoursopen(self):
        """
        method that prints timeopen values for every day in an organized way
        
        """
        print("""
            {} Hours:

            monday: {}
            tuesday: {}
            wednesday: {}
            thursday: {}
            friday: {}
            saturday: {}
            sunday: {}

            """.format(self.__bank_name, \
                       self.timeopen(1), \
                       self.timeopen(2), \
                       self.timeopen(3), \
                       self.timeopen(4), \
                       self.timeopen(5), \
                       self.timeopen(6), \
                       self.timeopen(0)))


    def change_timeopen(self, day, timeopen, timeclose):
        self.__bank_openhours[day] = timeopen
        self.__bank_closehours[day] = timeclose


    def add_customer(self, customer_obj):
        self.__customer_list["{}".format(customer_obj.get_customer_number()] = customer_obj

    def remove_customer(self, customer_obj):
        del self.__customer_list["{}".format(customer_obj.get_customer_number())]


    def add_employee(self, employee_obj):
        self.__employee_list["{}":.format(employee_obj.get_eid())] = employee_obj

    def remove_employee(self, employee_obj):
        del self.__employee_list["{}":.format(employee_obj.get_eid())]


    def isopen(self):
        __today = datetime.datetime.now()
        __weekdaytoday = datetime.datetime.weekday(__today)
        __currenttime = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)

        if self.__bank_openhours[__weekdaytoday] == None or self.__bank_closehours[__weekdaytoday] == None:
            print("{} is currently closed".format(self.__bank_name))

        elif __currenttime < self.__bank_openhours[__weekdaytoday] or __currenttime > self.__bank_closehours[__weekdaytoday]:
            print("{} is currently closed".format(self.__bank_name))
        else:
            print("{} is currently open.".format(self.__bank_name))
      
