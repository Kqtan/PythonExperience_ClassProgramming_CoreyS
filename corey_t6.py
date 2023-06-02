class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    # constructor - attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1

    # so, when we access the attributes
    # we do not need specify the parentheses (ie. emp_1.email())
    # but instead, we can write it like a normal attributes (ie. emp_1.email)
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    # name is the value we are trying to set
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    # delete the name of employee
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
        self.pay = None

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Kq", "Tan", 60000)

# when we change the details of an instance
# the email itself does not change with it 
# so, we are trying to find a way to update that shit in one shot
# if we create a function like fullname then it would break the code
# then we need smtg like decorators to help us out
# getters, setters, deleters
# property decorator
emp_1.first = "Dog"
# another case, we want to change the full name
emp_1.fullname = "Vitalik Buterin"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# delete shit
del emp_1.fullname
# kinda weird here
print(emp_1.email)