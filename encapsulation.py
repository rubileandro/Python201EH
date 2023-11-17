class Person:
    'Person base class'
    wants_to_escalate =  True

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print("My age is {}".format(self.__age))

    def birthday(self):
        self.__age += 1

bender = Person("age", 1000)
# print(bender.__age)
print(bender.get_age())
bender.set_age(1010)
print(bender.get_age())
bender.birthday()
print(bender.get_age())

# get around encapsulation
print(bender.__dict__)

bender._Person__age = 1500
print(bender.get_age())