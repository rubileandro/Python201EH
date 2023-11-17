class Person:
    'Person base class'
    wants_to_escalate =  True

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        self.__age = None

    @classmethod
    def wants_to(cls):
        return cls.wants_to_escalate
    
    @classmethod
    def bender_factory(cls):
        return cls("bender", 1005)
    
    @staticmethod
    def static_print():
        print("I am the same!")

    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print("My age is {}".format(self.__age))

    def birthday(self):
        self.__age += 1

bender = Person("bender", 1010)
print(bender.age)

bender.age = 1100
print(bender.age)

# del bender.age
# print(bender.age)

print(Person.wants_to_escalate)

bender1 = Person.bender_factory()
bender2 = Person.bender_factory()
bender3 = Person.bender_factory()

bender1.print_name()
bender2.print_name()
bender3.print_name()

Person.static_print()
bender1.static_print()
bender2.static_print()
bender3.static_print()
