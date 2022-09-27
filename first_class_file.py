class Customer:

    def set_name(self, new_name):
        # set the name attribute to new_name
        self.name = new_name

    # using the .name from the object itself
    def identify(self):
        print('I am Customer ' + self.name)

cust = Customer()
cust.set_name("Laura de Silva")
cust.identify()

cust2 = Customer()
cust2.set_name('Rashid Volkov')
cust2.identify()



#### another example ######
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

print(emp.name)
print(emp.salary)
