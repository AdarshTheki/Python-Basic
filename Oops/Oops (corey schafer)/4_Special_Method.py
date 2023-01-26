# Special Methods:-  (Magic/Dunder)

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay): # constructor
        self.first = first  # variables
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    
    def fullname(self): # methods
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('adarsh','verma',50000)
emp_2 = Employee('ayush','Verma',80000)

print(emp_1 + emp_2)    # 130000

print(len('test'))      # 4
print('test'.__len__()) # 4
print(len(emp_1))       # 12

print(repr(emp_1))  # Employee('adarsh','verma',50000)
print(str(emp_1))   # adarsh verma - adarsh.verma@company.com
print(emp_1)        # adarsh verma - adarsh.verma@company.com

print(1+2)              # 3
print(int.__add__(1,2)) # 3
print(str.__add__('a','b'))  # ab
