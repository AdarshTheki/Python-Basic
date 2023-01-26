# classes and Variables:-

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

emp_1 = Employee('adarsh','verma',50000)
emp_2 = Employee('ayush','Verma',80000)

print(emp_1.pay)    # 50000
emp_1.apply_raise()
print(emp_1.pay)    # 52000

print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)     # 1.04
print(emp_2.raise_amount)     # 1.04

print(Employee.__dict__)