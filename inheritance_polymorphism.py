# Core Principles of OOP

# Inheritance - > extending functionality of existing code
# Polymorphism -> creating a unified interface
# Encapsulation -> Bunding of data and methods

# Class-level data
class Employee:
    min_salary = 30000 # class-level attribute
    def __init__(self, name, salary):
        self.name = name
        if salary >= Employee.min_salary:
            self.salary = salary
        else:
            self.salary = Employee.min_salary


    # Class-level method
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name == f.readline()
        return cls(name)

emp1 = Employee("Harry Potter", 40000)
print(emp1.min_salary)
emp2 = Employee("Luna Lovegood", 60000)
print(emp2.min_salary)


#---------------------------- another example --------------------------------
print('Player example:')

class Player:
    max_position = 10
    max_speed = 3
    def __init__(self, position = 10):
        self.position = position

print(Player.max_position)
p=Player()
print(p.max_position)

p1, p2 = Player(), Player()
print('Max speed of p1 and p2 before assignment:')
print(p1.max_position)