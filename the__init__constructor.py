from datetime import datetime

# Constructor __init__() method is called every time an object is created

class Customer:
    def __init__(self, name, balance=0):
        print("The __init__ method was called")
        self.name = name
        if balance >= 0:
            self.balance = balance
        else:
            self.balance = 0
            print('Invalid balance!')

        self.hire_date = datetime.today()
        

cust = Customer("Laura de Silva")
print(cust.name)
print(cust.balance)
print(cust.hire_date)

cust2 = Customer("Lilian  Potter", 1000)
print(cust2.name)
print(cust2.balance)
print(cust.hire_date)


from math import sqrt

# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print('Error!')

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
