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

class Hacker(Person):
    def __init__(self, name, age, cves):
        super().__init__(name, age)
        self.cves = cves

    def print_name(self):
        print("My name is {} and I have {} CVE's".format(self.name, self.cves))
    
    def total_cves(self):
        return self.cves
    
bender = Person("bender", 1000)
leela = Hacker("fry", 35, 5)

bender.print_name()
leela.print_name()

print(bender.age)
print(leela.age)

bender.birthday()
leela.birthday()

print(bender.age)
print(leela.age)

print(leela.total_cves())
# print(bender.total_cves())

# retursn True if the given class is a sub-class of the parent class.
print(issubclass(Hacker, Person))
print(issubclass(Person, Hacker))

# returns True if the object is an instance of the class or if it's an instance of a subclass.
print(isinstance(bender, Person))
print(isinstance(bender, Hacker))

print(isinstance(leela, Person))
print(isinstance(leela, Hacker))
