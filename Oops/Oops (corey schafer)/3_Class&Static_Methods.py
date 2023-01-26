# Class Method and Static Methods

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = Employee('adarsh','verma',50000)
emp_2 = Employee('ayush','Verma',79000)

print(Employee.raise_amount)    # 1.04
print(emp_1.raise_amount)       # 1.04

Employee.set_raise_amt(1.05)    
print(Employee.raise_amount)    # 1.05
print(emp_1.raise_amount)       # 1.05

emp_str_1 = 'jone-verma-80000'
emp_str_2 = 'adarsh-verma-100000'
emp_str_3 = 'gopal-verma-20000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)      # jone.verma@company.com
print(new_emp_1.pay)        # 80000

import datetime
my_date = datetime.date(2020, 7, 10)
print(Employee.is_workday(my_date))  # True