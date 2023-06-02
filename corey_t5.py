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

    # unambiguous representation of an object
    # useful for debugging and delogging when doing programming
    # designed for the developers
    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # readable representation for the object
    # meant to be read by the end-user
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        # add 2 employees together then we get their total pay
        return self.pay + other.pay

    def __len__(self):
        # returning the length of fullname
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Kq", "Tan", 60000)

# str will have the higher order than repr in this case
# print(emp_1)

# weird - hen
print(repr(emp_1))
print(str(emp_1))

# same as this
print(emp_1.__repr__())
print(emp_1.__str__())

# magic method or the dunder method
# str or repr
print(1+2)
print(int.__add__(1, 2)) # gives the same result as above
print(str.__add__("a", "b")) # same as print("a"+"b")

# using the add method from the class
# there are multiple methods available in the documentation
print(emp_1 + emp_2)

# finding the length of a string
print(len("test"))
print("test".__len__())
print(len(emp_1))