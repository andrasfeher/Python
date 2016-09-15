class Person():
    # it is not necessary to have an __init__ method in every class definition;
    # it's used to do anything that's needed to distinguish this object from
    # others created from the same class
    # the first parameter must be self
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

class Car():
    def exclaim(self):
        print("I'm a Car!")

# inheritance ...
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

class Circle():
    def __init__(self, radius):
        self.radius = radius

    # limit the access to the attributes
    @property
    def diameter(self):
        return 2 * self.radius

# class variable and class method
class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, " little objects.")

# static method: you don't have to instantiate the class to use it
class Calculator():
    @staticmethod
    def add(a, b):
        print(a + b)

# special methods
class Word():
    def __init__(self, text):
        self.text = text

    # __eq__ is called automatically at comparision
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    # called automatically at print
    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'

# composition
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', bill.description, ' bill and a', tail.length, ' tail')

hunter = Person("Elmer Fudd")

print('The mighty hunter: ', hunter.name)

car = Car();
car.exclaim()

yugo = Yugo()
yugo.exclaim()

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

c = Circle(5)
print(c.radius)
print(c.diameter)

a1 = A()
a2 = A()
a3 = A()
A.kids()

Calculator.add(5, 6)


first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)
print(first)


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
