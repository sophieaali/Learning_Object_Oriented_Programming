class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet): # class Cat is inheriting the general class Pet
    # does not need an __init__  method bc it inherits the one from Pet()
    def speak(self):
        print('Meow')

class Dog(Pet):
    def __init__(self, name, age, color):
        # I've givin Dog an init method b.c it has an extra attribute
        super().__init__(name, age)
        self.color = color
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Bill", 34) # Cat() inherits the .show() method
c.show()
c.speak() # it will use the .speak() method from class Cat instead
d = Dog("Jill", 24, 'Pink')
d.show()
d.speak()
f = Fish("Bubbles", 2)
f.show()
f.speak()