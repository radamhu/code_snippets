
#!/usr/bin/env python3.6

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    # regular methodes in a class automatically take the instance as the 1st argument : calling this SELF
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    # as we receive the class as the first argument instead of instance
    # we called that CLS
    # it is just a function that takes another function as a parameter and returns another function
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.num_of_employees)

# it automatically accept the class, so we dont have to pass cls here just the amount variable
# run set_raise_amot methos which is a classmethod which means now we'r wroking w/ class instead of instance
Employee.set_raise_amt(1.05)
# equal Employee.raise_amt = 1.05

print(emp_1.raise_amount)
print(emp_2.raise_amount)


