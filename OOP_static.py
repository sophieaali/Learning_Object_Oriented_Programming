class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
print(p1.number_of_people)
p2 = Person("jill")
print(p2.number_of_people)


print(Person.number_of_people_())


# Static method example
class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run example")


print(Math.add5(5))
print(Math.add10(5))
Math.pr()