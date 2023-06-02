class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    # constructor - attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# trying to create different type of employees
# developers and managers
# subclasses - inheritance
# easier to maintain the codes when the project is getting larger
class Developer(Employee):
    # the method revolution order
    # find within this class first then only go to the class inherited
    # if it does not exist in this class then it would search in that order
    # simply inheriting the method from the parent class
    # change here does not affect the parent class
    # give flexibility in building the classes
    raise_amount = 1.10

    # passing programming language where other employees might not have
    # customising with just A LIL BIT of codes
    def __init__(self, first, last, pay, prog_lang):
        # do not want to repeat the codes
        # keeping the codes dry
        # let the super class handle these common attributes
        super().__init__(first, last, pay)
        # or Employee.__init__(self, first, last, pay) but not so maintainable
        # when we have multiple inheritance
        self.prog_lang = prog_lang

class Manager(Employee):
    # the employees the manager supervises
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # option to add and remove emp
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Kq", "Tan", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# information on the class - can get the method revolution order
print(help(Developer))
print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

####
# special stuff
print(isinstance(mgr_1, Manager)) # = True
print(isinstance(mgr_1, Employee)) # = True
print(isinstance(mgr_1, Developer)) # = False

print(issubclass(Manager, Employee)) # = True
print(issubclass(Manager, Developer)) # = False