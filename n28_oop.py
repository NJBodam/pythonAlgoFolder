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


# Alternative constructors
# Python allows you to define class methods as well, using the @classmethod decorator and a special first argument cls. The main use of class methods is defining methods that return an instance of the class, but aren't using the same code as __init__().

# For example, you are developing a time series package and want to define your own class for working with dates, BetterDate. The attributes of the class will be year, month, and day. You want to have a constructor that creates BetterDate objects given the values for year, month, and day, but you also want to be able to create BetterDate objects from strings like 2020-04-30.

# You might find the following functions useful:

# .split("-") method will split a string at"-" into an array, e.g. "2020-04-30".split("-") returns ["2020", "04", "30"],
# int() will convert a string into a number, e.g. int("2019") is 2019 .
# Instructions 1/2
# 50 XP
# 1
# 2
# Add a class method from_str() that:

# accepts a string datestr of the format'YYYY-MM-DD',
# splits datestr and converts each part into an integer,
# returns an instance of the class with the attributes set to the values extracted from datestr.

class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)


# For compatibility, you also want to be able to convert a datetime object into a BetterDate object.

# Add a class method from_datetime() that accepts a datetime object as the argument, and uses its attributes .year, .month and .day to create a BetterDate object with the same attribute values.

# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
        return cls(datetime.year, datetime.month, datetime.day)


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)


# Create a subclass
# The purpose of child classes -- or sub-classes, as they are usually called - is to customize and extend functionality of the parent class.

# Recall the Employee class from earlier in the course. In most organizations, managers enjoy more privileges and more responsibilities than a regular employee. So it would make sense to introduce a Manager class that has more functionality than Employee.

# But a Manager is still an employee, so the Manager class should be inherited from the Employee class.

# Instructions 1/2
# 50 XP
# 1
# 2
# Add an empty Manager class that is inherited from Employee.
# Create an object mng of the Manager class with the name Debbie Lashko and salary 86500.
# Print the name of mng

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass


# Define a Manager object
mng = Manager('Debbie Lashko', 86500)

# Print mng's name
print(mng.name)


# Create a subclass
# The purpose of child classes -- or sub-classes, as they are usually called - is to customize and extend functionality of the parent class.

# Recall the Employee class from earlier in the course. In most organizations, managers enjoy more privileges and more responsibilities than a regular employee. So it would make sense to introduce a Manager class that has more functionality than Employee.

# But a Manager is still an employee, so the Manager class should be inherited from the Employee class.

# Instructions 2/2
# 35 XP
# 2
# Remove the pass statement and add a display() method to the Manager class that just prints the string "Manager" followed by the full name, e.g. "Manager Katie Flatcher"
# Call the .display()method from the mnginstance.

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount      
        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print("Manager " + self.name)
  

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()



# Method inheritance
# Inheritance is powerful because it allows us to reuse and customize code without rewriting existing code. By calling methods of the parent class within the child class, we reuse all the code in those methods, making our code concise and manageable.

# In this exercise, you'll continue working with the Manager class that is inherited from the Employee class. You'll add new data to the class, and customize the give_raise() method from Chapter 1 to increase the manager's raise amount by a bonus percentage whenever they are given a raise.

# A simplified version of the Employee class, as well as the beginning of the Manager class from the previous lesson is provided for you in the script pane.

# Instructions 2/2
# 50 XP
# 2
# Add a give_raise() method to Manager that:

# accepts the same parameters as Employee.give_raise(), plus a bonus parameter with the default value of 1.05 (bonus of 5%),
# multiplies amount by bonus,
# uses the Employee's method to raise salary by that product.

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

# Customizing a DataFrame
# In your company, any data has to come with a timestamp recording when the dataset was created, to make sure that outdated information is not being used. You would like to use pandas DataFrames for processing data, but you would need to customize the class to allow for the use of timestamps.

# In this exercise, you will implement a small LoggedDF class that inherits from a regular pandas DataFrame but has a created_at attribute storing the timestamp. You will then augment the standard to_csv() method to always include a column storing the creation date.

# Tip: all DataFrame methods have many parameters, and it is not sustainable to copy all of them for each method you're customizing. The trick is to use variable-length arguments *args and **kwargsto catch all of them.

# Instructions 1/2
# 0 XP
# 1
# 2
# Import pandas as pd.
# Define LoggedDF class inherited from pd.DataFrame.
# Define a constructor with arguments *args and **kwargs that:
# calls the pd.DataFrame constructor with the same arguments,
# assigns datetime.today() to self.created_at

# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)


# Customizing a DataFrame
# In your company, any data has to come with a timestamp recording when the dataset was created, to make sure that outdated information is not being used. You would like to use pandas DataFrames for processing data, but you would need to customize the class to allow for the use of timestamps.

# In this exercise, you will implement a small LoggedDF class that inherits from a regular pandas DataFrame but has a created_at attribute storing the timestamp. You will then augment the standard to_csv() method to always include a column storing the creation date.

# Tip: all DataFrame methods have many parameters, and it is not sustainable to copy all of them for each method you're customizing. The trick is to use variable-length arguments *args and **kwargsto catch all of them.

# Instructions 2/2
# 50 XP
# 2
# Add a to_csv() method to LoggedDF that:
# copies self to a temporary DataFrame using .copy(),
# creates a new column created_at in the temporary DataFrame and fills it with self.created_at
# calls pd.DataFrame.to_csv() on the temporary variable.

# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created_at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)

# Incredible work! Using *args and **kwargs allows you to not worry about keeping the signature of your customized method compatible. Notice how in the very last line, you called the parent method and passed an object to it that isn't self. When you call parent methods in the class, they should accept _some_ object as the first argument, and that object is _usually_ self, but it doesn't have to be!


# Writing a class for your package
# We've covered how classes can be written in Python. In this exercise, you'll be creating the beginnings of a Document class that will be a foundation for text analysis in your package. Once the class is written you will modify your package's __init__.py file to make it easily accessible by your users.

# Below is the structure of where you'll be working.

# working_dir
# ├── text_analyzer
# │    ├── __init__.py
# │    ├── counter_utils.py
# │    ├── document.py
# └── my_script.py
# Instructions 1/2
# 50 XP
# 1
# 2
# You are working in document.py.
# Finish the def statement that will create a new Document instance when a user calls Document().
# Use your knowledge of PEP 8 conventions to complete the definition of the newly named class method.

# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text

# Writing a class for your package
# We've covered how classes can be written in Python. In this exercise, you'll be creating the beginnings of a Document class that will be a foundation for text analysis in your package. Once the class is written you will modify your package's __init__.py file to make it easily accessible by your users.

# Below is the structure of where you'll be working.

# working_dir
# ├── text_analyzer
# │    ├── __init__.py
# │    ├── counter_utils.py
# │    ├── document.py
# └── my_script.py
# Instructions 2/2
# 50 XP
# Question
# You just completed writing the Document class for your package in document.py. Which of the following lines would correctly import this class in __init__.py using relative import syntax?

from .document import Document

# import your text_analyzer package.
# Create an instance of Document with the datacamp_tweet variable that's been loaded into your session.
# Print the contents of the text attribute of your newly created Document instance.

# Import custom text_analyzer package
import text_analyzer

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)



# Adding functionality to a child class
# You've just written a SocialMedia class that inherits functionality from Document. As of now, the SocialMedia class doesn't have any functionality different from Document. In this exercise, you will build features into SocialMedia to specialize it for use with Social Media data.
# For reference, the definition of Document can be seen below.
# class Document:
#     # Initialize a new Document instance
#     def __init__(self, text):
#         self.text = text
#         # Pre tokenize the document with non-public tokenize method
#         self.tokens = self._tokenize()
#         # Pre tokenize the document with non-public count_words
#         self.word_counts = self._count_words()

#     def _tokenize(self):
#         return tokenize(self.text)

#     # Non-public method to tally document's word counts
#     def _count_words(self):
#         # Use collections.Counter to count the document's tokens
#         return Counter(self.tokens)

# Instructions 2/2

# 	•	Fill in the first line ofSocialMedia's __init__ method using the parent class to properly utilize inheritance.
# 	•	Properly call the _count_mentions method in __init__ to add a new feature to SocialMedia.


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')



# Using your child class
# Thanks to the power of inheritance you were able to create a feature-rich, SocialMedia class based on its parent, Document. Let's see some of these features in action.

# Below is the full definition of SocialMedia for reference. Additionally, SocialMedia has been added to __init__.py for ease of use.

# class SocialMedia(Document):
#     def __init__(self, text):
#         Document.__init__(self, text)
#         self.hashtag_counts = self._count_hashtags()
#         self.mention_counts = self._count_mentions()

#     def _count_hashtags(self):
#         # Filter attribute so only words starting with '#' remain
#         return filter_word_counts(self.word_counts, first_char='#')      

#     def _count_mentions(self):
#         # Filter attribute so only words starting with '@' remain
#         return filter_word_counts(self.word_counts, first_char='@')
# Instructions
# 100 XP
# import your text_analyzer custom package.
# Define dc_tweets as an instance of SocialMedia with the preloaded datacamp_tweets object as the text.
# print the 5 most_common mentioned users in the data using the appropriate dc_tweets attribute.
# Use text_analyzer's plot_counter() method to plot the most used hashtags in the data using the appropriate dc_tweets attribute.
# Import custom text_analyzer package
import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)


# Creating a grandchild class
# In this exercise you will be using inheritance to create a Tweet class from your SocialMedia class. This new grandchild class of Document will be able to tackle Twitter specific details such as retweets.

# Instructions
# 100 XP
# Complete the class statement so that Tweets inherits from SocialMedia. SocialMedia has already been loaded in your environment.
# Use super() to call the __init__ method of the parent class.
# Define retweet_text. Use help() to complete the call to filter_lines with the correct parameter name. filter_lines has already been loaded in your environment.
# return retweet_text from _process_retweets as an instance of SocialMedia

# Define a Tweet class that inherits from SocialMedia# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(self, text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)

# Using inherited methods
# You've now defined a Tweets class that's inherited methods from both Document and SocialMedia. In this exercise, you'll use inherited methods to visualize text from both tweets and retweets.

# Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).

# Instructions 3/3
# 30 XP
# 3
# Use the plot_counts() method of the retweets attribute to plot the most used hashtags in the retweets subset of the data.

# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')


# In Python, the timeit module provides a convenient way to measure the execution time of small code snippets. You can use the timeit.timeit() function to time the execution of a specific piece of code or function. Here's how to use it

import timeit

# Define the code or function you want to time
code_to_time = """
for i in range(1000):
    result = i * 2
"""

# Measure the execution time
execution_time = timeit.timeit(stmt=code_to_time, number=1000)

# %timeit code_to_time(*args)

# Print the execution time
print(f"Execution time: {execution_time} seconds")


# Using %lprun: spot bottlenecks
# Profiling a function allows you to dig deeper into the function's source code and potentially spot bottlenecks. When you see certain lines of code taking up the majority of the function's runtime, it is an indication that you may want to deploy a different, more efficient technique.
# Lets dig deeper into the convert_units() function.
# def convert_units(heroes, heights, weights):

#     new_hts = [ht * 0.39370  for ht in heights]
#     new_wts = [wt * 2.20462  for wt in weights]

#     hero_data = {}

#     for i,hero in enumerate(heroes):
#         hero_data[hero] = (new_hts[i], new_wts[i])

#     return hero_data
# Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units() function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a -f flag specifying the function you'd like to profile).
# The convert_units() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:
# What percentage of time is spent on the new_hts list comprehension line of code relative to the total amount of time spent in the convert_units() function?


# In [1]: %load_ext line_profiler
# In [2]: %lprun -f convert_units convert_units(heroes, hts, wts)



# Using %mprun: Hero BMI
# You'd like to calculate the body mass index (BMI) for a selected sample of heroes. BMI can be calculated using the below formula:

# BMI = mass(kg) / height(m)^2

# A random sample of 25,000 superheroes has been loaded into your session as an array called sample_indices. This sample is a list of indices that corresponds to each superhero's index selected from the heroes list.

# A function named calc_bmi_lists has also been created and saved to a file titled bmi_lists.py. For convenience, it is displayed below:

# def calc_bmi_lists(sample_indices, hts, wts):

#     # Gather sample heights and weights as lists
#     s_hts = [hts[i] for i in sample_indices]
#     s_wts = [wts[i] for i in sample_indices]

#     # Convert heights from cm to m and square with list comprehension
#     s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

#     # Calculate BMIs as a list with list comprehension
#     bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

#     return bmis
# Notice that this function performs all necessary calculations using list comprehension (hence the name calc_bmi_lists()). Dig deeper into this function and analyze the memory footprint for performing your calculations using lists:

# Load the memory_profiler package into your IPython session.
# Import calc_bmi_lists from bmi_lists.
# Once you've completed the above steps, use %mprun to profile the calc_bmi_lists() function acting on your superheroes data. The hts array and wts array have already been loaded into your session.
# After you've finished coding, answer the following question:

# How much memory do the list comprehension lines of code consume in the calc_bmi_lists() function? (i.e., what is the total sum of the Increment column for these four lines of code?)



# %load_ext memory_profiler
from bmi_lists import calc_bmi_lists
# %mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

