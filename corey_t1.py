# Python OOP
# learning about creating, and instantiating simple classes
"""
logically group our data and function
attributes and methods
methods - function associated with a class

class and instance in class
class is a blueprint
"""

# employee as an object
class Employee:
    # creating a class variable, something that every instance shares in common
    raise_amount = 1.04
    num_of_emps = 0

    # constructor - attributes
    def __init__(self, first, last, pay):
        # we can actually create email using first and last
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        # the case where self is useless, since the increment of num of emps is the freaking same
        Employee.num_of_emps += 1

    # adding methods to the class
    # you can do it manually but it will be so, so, so troublesome
    # a function in a class, always takes the first argu as the instance (self)
    # make sure you put self as the first arguments
    def fullname(self):
        # self is the instance, easy way to do shit
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # using self.raise_amount gives us the ability to change the variable anytime
        self.pay = int(self.pay * self.raise_amount)

    # no need to take self as the first arguments
    # adding decorator
    # decorator alter the function that takes the first argument as class
    # instead of self (instance)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # splitting using hypen
        first, last, pay = emp_str.split("-")
        # this thing will create the employee
        # and rmb to return to fulfill the assignment as alternative constructor
        return cls(first, last, pay)

    # static method don't place anything as the first argument
    # unlike the normal method or classmethod
    # things that have some connection with the class but
    # they do not actually need the instance or class to work
    # it basically behaves like a normal function
    @staticmethod
    def is_workday(day):
        # Python have the weekday methods
        # Monday is 0, Sunday is 6 and so on
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# instances, they are both employee but different object/instances
# we can pass in values using the init method
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Kq", "Tan", 60000)

# we can create them manually
emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000
# if we dont want to do it this way then we can use attributes in a class
print(emp_1.email)
print(emp_2.email)


# manually to get the fullname
print("{} {}".format(emp_1.first, emp_1.last))
# using class
print(emp_1.fullname()) # or
Employee.fullname(emp_1) # it is the same way of passing

# staticmethod and classmethods
# class method - whole class updated
Employee.set_raise_amt(1.05) # equals to Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)

# solving problems like passing one whole string
# and the class automatically initialise itself
# instead of parsing it one by one
# classmethods can be alternative constructor, just like __init__
emp_str_1 = 'John-Doe-70000'
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# pass in the string and get the same result
new_emp_1 = Employee.from_string(emp_str_1)

# to illustrate the example of static method
import datetime
my_date = datetime.date(2023, 6, 2)

print(Employee.is_workday(my_date))