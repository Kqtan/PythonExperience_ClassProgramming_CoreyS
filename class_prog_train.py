class Person:
    # adding something that a person will have
    # we are creating an object person then they have attributes like age
    # important concept in oop or object oriented programming
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase
    
    # Besides, we can also add method into a class
    # which is super useful for creating an object that allows others to use
    # like an endpoint available to everyone
    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

# creating a person (ie creating an object)
user = Person(25, 80, 180, "Jon", "Dick", "Yo!")
print(user.catch_phrase)

# call the method
user.walk()