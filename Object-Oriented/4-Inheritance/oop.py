
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # same
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Mangaer(Employee):

    def __init__(self, first, last, pay, employess=None):
        super().__init__(first, last, pay)
        # same
        # Employee.__init__(self, first, last, pay)
        if employess is None:
            self.employees = []
        else:
            self.employees = employess

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Test', 'Employee', 60000, 'java')

mgr_1 = Mangaer('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Developer))
print(issubclass(Mangaer, Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
