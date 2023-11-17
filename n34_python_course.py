

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
hour = int(input("Enter the hour: "))
min = int(input("Enter the minute: "))

min_in_hour= int(60)
hours_in_day = int(24)
days_in_month = int(30)
month_in_year = int(12)

m = year * month_in_year + month # month in total
d = m * days_in_month + day
h = d * hours_in_day + hour
result_min = h * min_in_hour + min

print(f"{day}.{month}.{year} {hour}.{min} is {result_min}")




# 
# n = input("Enter a number >= 0: ")
# n = int(n)
# 
# counter = 0
# 
# while counter <= n:
#     powerk = 2**counter
#     print(f"2**{counter} == {powerk}")
#     counter +=1
#     

# Block (Instruction Blocks)


# Exercise 1

# Write a script that
# let the user enter a positive integer number (<10)
# if the number is larger than your upper bound, print it in digits
# prints the number in letters
# The output should look like that:

# >>> %Run ex023_numbertext.py
# Enter a positive number <= 10: 7
# 7 == Seven
# or
# >>> %Run ex023_numbertext.py
# Enter a positive number <= 10: 20
# 20 == 20

 
# Hints:
# In this task you exercise
# the if-elif-Statement to switch between different cases
numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
number = input("Enter a positive number: ")

num = int(number)
if num < 10:
    print(numbers[num - 1])
else:
    print(number)


# Exercise 2

# We assume a simple calendar with all months having 30 days.

# Write ascript
# let the user enter a number (which represents a time span from 01.01.0000 in minutes)
# convert the number into an int-value
# compute the represented date and time
# The output should look like this
# This script transforms a positive integer number into years, months, days, hours and minutes since 01.01.0000.
# Please enter an int-number>0: 1049190255
# Result: 1049190255 minutes = 2023 years, 10 months, 24 days, 8 hours, and 15 minutes.

# Hints:
# In this task you exercise
# entering values and printing messages
# converting Strings to int-numbers
# Expressions with multiplication and integer division (//) and remainder (%)
# variables and assignments
# if-statement (optionally)


def date_time_converter(time):
    

    year_static = 12
    month_static = 30
    day_static = 24
    minute_static = 60
    
    year_in_min = 518400
    month_in_min = 43200
    day_in_min = 1440
    hour_in_min = 60
    
    
    year = time // year_in_min
    
    month = (time % year_in_min) // month_in_min
    
    day = ((time % year_in_min) % month_in_min) // day_in_min
    
    hour = (((time % year_in_min) % month_in_min) % day_in_min) // hour_in_min

    remaining = time % 60
    
    
    print(f"{year} years, {month} months, {day} days, {hour} hours, and {remaining} minutes.")

import datatime

# def minutes_years_months_converter(minutes):
    
#     seconds = minutes * 60
    
#     time_delta = datetime.timedelta(seconds=seconds)

n = input("")
def fibonacci_seq(n):    
    if n <= 1:
        print(n)
    else:
        f2 = 0
        f1 = 1
        while n > 1:
            temp = f1 + f2
            f2 = f1
            f1 = temp
            n = n -1
        return f1




# Exercise 3

# Welcome to the Sensor Data Management App (V0.1)!
# Please enter ...
#     the name of the sensor: CO2
#     the unit of the sensor's measurements: μg/m³
#     the time step of the measurements (in minutes): 655
# The time span between measurements is 0 days 10 hours 55 minutes.

# Please enter ...
#     the year of the measurement: 2023
#     the month (as int) of the measurement: 30
#     the day of the measurement: 11
#     the hour of the measurement: 20
#     the minute of the measurement: 15
#     the measured value (float): 73.0
# Sensor CO2 measured 73.0μg/m³ on 11.30.2023 at 20:15 h.
# The next measurement will be on 12.6.2025 at 7:10 h.
    
import datetime


print("Welcome to the Sensor Data Management App (V0.1)!")
print("Please enter ...")

name= str(input("the name of the sensor: "))
unit= str(input("the unit of the sensor's measurements: "))
time= int(input("the time step of the measurements (in minutes): "))


hour= time // 60
day= hour // 24
remaining = time % 60

timespan = datetime.timedelta(hours=hour, days=day, minutes=remaining)

print(f"The time spam between measurements is {day} days {hour} hours {remaining} minutes.")


print("Please enter ...")
year= int(input("the year of the measurement: "))
month= int(input("the month of the measurement: "))
day= int(input("the day of the measurement: "))
hour= int(input("the hour of the measurement: "))
minutes= int(input("the minute of the measurement: "))
value= float(input(" the measured value (float): "))

measure_date = "{}.{}.{}.{}:{}".format(year, month, day, hour, minutes)
date = datetime.datetime(year, month, day, hour, minutes)

next_measure = date + timespan

# next_date = datetime.datetime.strptime(next_measure.date(), '%d-%m-%Y')

next_date = next_measure.date().strftime('%d.%m.%Y')

next_time = next_measure.time().strftime('%H:%M')
print(next_date)
print(next_time)
#time1 = dt.strptime(, "%H%M").hour

#date1 = dt.strptime(measure_date, '%Y-%m-%d-%H:%M')

print(f"Sensor '{name}' measured {value}{unit} on {day}.{month}.{year} at {hour}.{minutes} h")
print(f"The next measurement will be on {next_date} at {next_time} h.")



#sensor


# Often an algorithm affords that the user should enter a value in a specific range (e.g. "yes" or "no" or a number in a given range).
# Aborting the script, if the user hasn't entered a correct value, is very frustrating.
# It is better, to give the user another chance:

# Write a Python script that lets the user enter a number which must be in the range from 0 to 10.
# If the number is not in the range print an error message and ask for a new value
# until the number is in the correct range.

# The output should look like that:
# Please enter a value in range 0..10: 17
# 17 is not in the range 0..10 - try again!
# Please enter a value in range 0..10: -5
# -5 is not in the range 0..10 - try again!
# Please enter a value in range 0..10: 7
# You have entered 7 which in the range 0..10 - thank you!

# INCOMPLETE
def getval():
    value = int(input("Please enter a value in range 0..10: "))

    while value > 10 or value < 0:
        print(f"{value} is not in the range 0..10 - try again!")
        value = int(input("Please enter a value in range 0..10: "))
    
    print(f"You have entered {value} which in the range 0..10 - thank you!")

try:
    getval()

except Exception as ve:
    print(f" is not in the range 0..10 - try again!")
    value = int(input("Please enter a value in range 0..10: "))


# Write a Python program
# which reads an integer  number from the input and stores it in a variable named height .
# and prints a triangle of "*" which has height lines.
# For height == 5 the output should look like that :
#     *
#    ***
#   *****
#  *******
# *********
# ---------
# Upload your python Program here.

# Hints:
# Remember that Strings can be multiplied by int numbers: "*" * 3  is the same as "***"
# Use a variable starting with value 0 and increment its value by 1 in each iteration of the while loop until it is equal to height.
# For computing the indentation, experiment with some example drawings, e.g.
# How many stars have to be printed in the first line?
# If n stars are printed in the last line, how many mor must be printed in the next one?
# How many stars do you have to print in line height?
# How does the number of blanks on the left of the stars change from one line to the next?

value = int(input("Enter height value: "))
triangle = range(1, value * 2, 2)
index = 0

while index < len(triangle):
    spaces = len(triangle) - index
    print(" " * spaces + "*" * triangle[index])
    index += 1
    
print(" " + "-" * triangle[index - 1])

# for i in range(1, value + 1):
#     spaces = value - i
#     print(" " * spaces + "* " * i)


# Write reads a program which prints a song: It goes like this until a given number of man is reached:

# 1 man went to mow
# Went to mow a meadow;
# 1 man and his dog, Spot
# Went to mow a meadow

# 2 men went to mow
# Went to mow a meadow;
# 2 men, 1 man and his dog, Spot
# Went to mow a meadow
# ...
# 9 men  went to mow
# Went to mow a meadow;
# 9 men, 8 men, 7 men, 6 men, 5 men, 4 men, 3 men, 2 men, 1 man and his dog, Spot
# Went to mow a meadow

# Write a Python program which
# reads the maximum number of men,
# stores it in variable max_men,
# and prints all verses of this song (the output should look like above)
# Extended Version:
# Write the numbers as text (see task before)  instead of digits
# Hints:
# Assign texts which are repeated in each verse to variables to keep your statements short and easy to read.
# Assume a fixed numer of men, e.g. maxMen = 4 and
# solve the subproblem of printing the count down-line "4 men, 3 men, 2 men, 1 man and his dog, Spot" first
# Start with an empty String: countdownline = ""
# Count the number n down in a loop and append the numbers (n) and text ("men") to this String: 

# countdownline = ... + countdownline   
 
# Do not forget that numbers must be casted to Strings by str() to concatenate them with the String in countdownline
# Use an if-Statement to choose the text  ("men" or "man and his dog, Spot")
 
# Complete Script: There are two alternatives to solve this task
# You may use  two counters in two nested loops:
# the first one counts up from 1 to max_men for each verse.
# the second one counts down from the current number of men downto 1 in each verse (countdownline-subproblem from before).
# or do it all in one loop
# the trick is to build the countdownline from right to left:
# countdownline = ... + countdownline
# Advanced versions (Extra point) :
# Can you avoid that the user enters a negative number or 0? (Reuse  the script from the second task and adapt it.)
# Can you print the numbers <= 10  as text? (Reuse the script of the first task and adapt it if necessary.)
# Hints:
# In this task you exercise
# input and output, formatted Strings
# While-loop and if-statement, nested Loops
# constructing strings iteratively from the left to the right or vice versa

max_men = int(input("Enter number of men: "))
print("")
index = 1

verse1 = " went to mow \nWent to mow a meadow \n"
verse2 = " and his dog, Spot \nWent to mow a meadow \n"

# try:
#     max_men = int(max_men)
#     if max_men < 0:
#         max_men = int(input("Enter number of men: "))
# except ValueError:
#     print(f"{n} is not a number. Please try again.")
#     max_men = int(input("Enter number of men: "))


while max_men <= 0:
    max_men = int(input("Enter number of men: "))
    print("")

while index <= max_men:
    
    if index == 1:
        print(str(index) + " man" + verse1 + str(index) + " man" + verse2)
    
    elif index > 1 and index < max_men:
        print(str(index) + " men" + verse1 + str(index) + " men" + verse2)
        
    elif index == max_men :
        sub_index = index
        print(str(index) + " men" + verse1, end="")
        while sub_index > 1:
            print(str(sub_index) + " men", end=" ")
            sub_index -= 1
        print("1 man and his dog, Spot")
    
    index += 1


# Sensors deliver values each timestep.
# So, for each new measurement, you can compute the time by adding the timestep instead of letting the user enter the date again.
# Write a script which asks the user for date and time (as in script "").
# Ask if the user wants to enter another value (y/n)
# In a loop: while the user has entered "y" or "Y"
# Compute and print the correct date and time which is exactly timestep minutes later. (We assume a simplified calendar with 30 days per each month.)
# and ask for a new value
# and print date, time and value.
# The output should look like:
# Welcome to the Sensor Data Management App (V0.1)!
# Please enter ...
#      the name of the sensor: CO2
#      the unit of the sensor's measurements: μg/m³
#      the time step of the measurements (in minutes): 1515
# The time span between measurements is 1 days 1 hours 15 minutes.

# Please enter ...
#      the year of the first measurement: 2023
#      the month (as int) of the measurement: 9
#      the day of the measurement: 29
#      the hour of the measurement: 22
#      the minute of the measurement: 10
#      the measured value (float): 10
# Sensor CO2 measured 10.0μg/m³ on 29.9.2023 at 22:10 h.

# Do you want to enter another value? (y/n): y
# The next measurement is on 30.9.2023 at 23:25 h.
# Please enter the measured value (float): 13
# Sensor CO2 measured 13.0μg/m³ on 30.9.2023 at 23:25 h.

# Do you want to enter another value? (y/n): y
# The next measurement is on 2.10.2023 at 0:40 h.
# Please enter the measured value (float): 15
# Sensor CO2 measured 15.0μg/m³ on 2.10.2023 at 0:40 h.

# Do you want to enter another value? (y/n): n


import datetime



import datetime


print("Welcome to the Sensor Data Management App (V0.1)!")

print("Please enter ...")

name= str(input("the name of the sensor: "))
unit= str(input("the unit of the sensor's measurements: "))
time= int(input("the time step of the measurements (in minutes): "))


day = round(time // 1440)
hour = round((time % 1440) // 60)
remaining = time % 60

timespan = datetime.timedelta(hours=hour, days=day, minutes=remaining)

print(f"The time step between measurements is {day} days {hour} hours {remaining} minutes.")


print("Please enter ...")
year= int(input("the year of the measurement: "))
month= int(input("the month (as int) of the measurement: "))
day= int(input("the day of the measurement: "))
hour= int(input("the hour of the measurement: "))
minutes= int(input("the minute of the measurement: "))
value= float(input("the measured value (float): "))

measure_date = "{}.{}.{}.{}:{}".format(year, month, day, hour, minutes)
date = datetime.datetime(year, month, day, hour, minutes)

next_measure = date + timespan

next_date = next_measure.date().strftime('%d.%m.%Y')
next_time = next_measure.time().strftime('%H:%M')

print(f"Sensor '{name}' measured {value}{unit} on {day}.{month}.{year} at {hour}.{minutes} h")
print("")

ans = "y"

while ans.lower() == "y":
    ans = input("Do you want to enter another value? (y/n): ")
    if(ans.lower() == "n"):
        break
    print(f"The next measurement will be on {next_date} at {next_time} h.")
    value= float(input("Please enter the measured value (float): "))
    print(f"Sensor {name} measured {value}{unit} on {next_date} at {next_time} h.")
    print("")
    next_measure += timespan
    next_date = next_measure.date().strftime('%d.%m.%Y')
    next_time = next_measure.time().strftime('%H:%M')

# Write a script which prints the ABC:
# ‒ This could be done with a while-Loop

letter_str = ""
code = ord("A")
while code <= ord("Z"):
   letter = chr(code)
   code += 1
   letter_str += letter + " "



# 1
# Code an unsigned value in binary representation
# Let the user enter a positive  int number (including 0)
# ensure that a positive value (>=0) has been entered!
# Store the base 2 in a variable called new_base
# Compute the  representation of the number in base new_base (see slide 110) and print the new representation.
# The binary digits should be in the correct order!
# (see Task "One man went to mow", where we built a String by concatenating parts of it in a loop)
# What happens if you change new_base to another value , e.g.
# new_base = 7  or
# new_base = 1 or
# new_base = 0 ?
# Answer this question in the comment field.
# Hints:
# In this task, you exercise:
# binary representation of unsigned numbers
# control structures


# 2
    
# Coding unsigned integers with an arbitrary base2 points
# Enhance your former program:
# The new_base should be allowed to be a positive int number in the range (2 .. 20).
#  ask the user to enter the base and give an error message if a wrong value has been entered (until the user enters a correct one)
# As beforre: Compute the representation of an entered positive  number to the base new_base.
# Replace digits in the new representation which are larger than 9 by  capital letters 'A', 'B', ... before printing the new representation.

# Hints:
# The values of the letters A-F are:  10 ~ A, 11~ B, 12~ C, 13~ D, 14~ E, 15 ~ F, ..
# The Unicodes or ASCII-codes of the capital letters are increasning number:  ord('A') = 65, ord('B') = 66,.. . You can use this to calculate the letter instead of having a switch-statement!
# Hints:
# In this task, you exercise:
# hexadecimal (base = 16)  representation of unsigned numbers
# control structures
# Unicodes of letters
