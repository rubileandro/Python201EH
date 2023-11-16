class Person:
    'Person base class'
    wants_to_escalate =  True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print("My age is {}".format(self.age))

    def birthday(self):
        self.age += 1
    

bender = Person("bender", 1000)
leela = Person("leela", 36)
fry = Person("fry", 36)

print(bender)
print(leela)
print(fry)

bender.print_name()
leela.print_name()
fry.print_name()

bender.print_age()
leela.print_age()
fry.print_age()

bender.age = 1008
bender.print_age()

bender.birthday()
bender.print_age()


print(bender.name)
print(bender.age)

# check attribute
print(hasattr(bender, "age"))
print(hasattr(bender, "asd"))

# check object value
print(getattr(bender, "age"))

# set attribute
setattr(bender, "asd", 1005)

print(getattr(bender, "asd"))

delattr(bender, "asd")

# print(getattr(bender, "asd"))

print(Person.wants_to_escalate)
print(bender.wants_to_escalate)
print(leela.wants_to_escalate)
print(fry.wants_to_escalate)

Person.wants_to_escalate = "No way!"

print(Person.wants_to_escalate)
print(bender.wants_to_escalate)
print(leela.wants_to_escalate)
print(fry.wants_to_escalate)

Person.wants_to_escalate = "Hell Yeah!"

print(Person.wants_to_escalate)
print(bender.wants_to_escalate)
print(leela.wants_to_escalate)
print(fry.wants_to_escalate)

bender.print_name()
del bender.name
# bender.print_name()

# del Person
# print(leela.name)

leela2 = Person("leela2", 35)

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
