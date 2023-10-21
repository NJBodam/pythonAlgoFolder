# Create your first class
# Time to write your first class! In this exercise, you'll start building the Employee class you briefly explored in the previous lesson. You'll start by creating methods that set attributes, and then add a few methods that manipulate them.

# As mentioned in the first video, an object-oriented approach is most useful when your code involves complex interactions of many objects. In real production code, classes can have dozens of attributes and methods with complicated logic, but the underlying structure is the same as with the most simple class.

# Your classes in this course will only have a few attributes and short methods, but the organizational principles behind the them will be directly translatable to more complicated code.

# Instructions 1/3
# 25 XP
# 1
# 2
# 3
# Create an empty class Employee.
# Create an object emp of the class Employee by calling Employee().
# Try printing the .name attribute of emp object in the console. What happens?

# Create an empty class Employee
class Employee:
    pass


# Create an object emp of class Employee 
emp = Employee()
print(emp.name)


# Modify the Employee class to include a .set_name() method that takes a new_name argument, and assigns new_name to the .name attribute of the class.
# Use the set_name() method on emp to set the name to 'Korel Rossi'.
# Print emp.name.

# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name("Korel Rossi")

# Print the name of emp
print(emp.name)


# Follow the pattern to add another method - set_salary() - that will set the salary attribute of the class to the parameter new_salary passed to method.
# Set the salary of emp to 50000.
# Try printing emp.salary before and after calling set_salary().

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

print(emp.salary)



# Print the salary attribute of emp.
# Attributes aren't read-only: use assignment (equality sign) to increase the salary attribute of emp by 1500, and print it again.


class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, new_salary):
        self.salary += new_salary 


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)


# Methods don't have to just modify the attributes - they can return values as well!

# Add a method monthly_salary() that returns the value of the .salary attribute divided by 12.
# Call .monthly_salary() on emp, assign it to mon_sal, and print.

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12

    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)


# Define the class Employee with a constructor __init__() that:

# accepts two arguments, name and salary (with default value0),
# creates two attributes, also called name and salary,
# sets their values to the corresponding arguments.

class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary) 


# The __init__() method is a great place to do preprocessing.

# Modify __init__() to check whether the salary parameter is positive:
# if yes, assign it to the salary attribute,
# if not, assign 0 to the attribute and print "Invalid salary!"

class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
            self.salary = salary
        else:
            print("Invalid salary!")
            self.salary = 0
   
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# Import datetime from the datetime module. This contains the function that returns current date.
# Add an attribute hire_date and set it to datetime.today().

# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)


# Write the class Point as outlined in the instructions
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        if x > 0 or y > 0:
            self.x = x
            self.y = y
        else:
            self.x = 0.0
            self.y = 0.0

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("An error message")


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())


# Define a class Player that has:
# A class attribute MAX_POSITION with value 10.
# The __init__() method that sets the position instance attribute to 0.
# Print Player.MAX_POSITION.
# Create a Player object p and print its MAX_POSITION.

# Create a Player class
class Player:

    MAX_POSITION = 10

    def __init__(self, postion=0):
        self.postion = postion


# Print Player.MAX_POSITION       
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.postion)


# Add a move() method with a steps parameter such that:

# if position plus steps is less than MAX_POSITION, then add steps to position and assign the result back to position;
# otherwise, set position to MAX_POSITION.
# Take a look at the console for a visualization!

class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps=0):
        if (self.position + steps) < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION

    

       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()