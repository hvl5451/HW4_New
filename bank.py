import datetime
from employee import Employee

class Bank:

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
        return self.__bank_name
    
    def get_customer_list(self):
        return self.__customer_list
    
    def get_employee_list(self):
        return self.__employee_list
    
    
    def timeopen(self, day):
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
      
