# Project Instructions
# The LAPD has asked you to help them by finding answers to the following questions:

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
# Which area has the largest frequency of night crimes (crimes committed between 10pm and 4am)? Save as a string variable called peak_night_crime_location.
# Identify the number of crimes committed against victims by age group (<18, 18-25, 26-34, 35-44, 45-54, 55-64, 65+). Save as a pandas Series called

# You have been asked to support the Los Angeles Police Department (LAPD) by analyzing crime data to identify patterns in criminal behavior. They plan to use your insights to allocate resources effectively to tackle various crimes in different areas.

# The Data
# They have provided you with a single dataset to use. A summary and preview are provided below.

# It is a modified version of the original data, which is publicly available from Los Angeles Open Data.

# crimes.csv
# Column	Description
# 'DR_NO'	Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits.
# 'Date Rptd'	Date reported - MM/DD/YYYY.
# 'DATE OCC'	Date of occurrence - MM/DD/YYYY.
# 'TIME OCC'	In 24-hour military time.
# 'AREA NAME'	The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.
# 'Crm Cd Desc'	Indicates the crime committed.
# 'Vict Age'	Victim's age in years.
# 'Vict Sex'	Victim's sex: F: Female, M: Male, X: Unknown.
# 'Vict Descent'	Victim's descent:
# A - Other Asian
# B - Black
# C - Chinese
# D - Cambodian
# F - Filipino
# G - Guamanian
# H - Hispanic/Latin/Mexican
# I - American Indian/Alaskan Native
# J - Japanese
# K - Korean
# L - Laotian
# O - Other
# P - Pacific Islander
# S - Samoan
# U - Hawaiian
# V - Vietnamese
# W - White
# X - Unknown
# Z - Asian Indian
# 'Weapon Desc'	Description of the weapon used (if applicable).
# 'Status Desc'	Crime status.
# 'LOCATION'	Street address of the crime.

# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()

# Start coding here
# Use as many cells as you need
from collections import Counter

# night_time_1 = crimes[crimes['TIME OCC'] > '2200']
# night_time_2 = crimes[crimes['TIME OCC'] < '0400']
# night_time_df = pd.concat([night_time_1, night_time_2], ignore_index=True)

# peak_night_crime_location = night_time_df['AREA NAME'].value_counts()

# Start coding here
# Use as many cells as you need
from collections import Counter
from datetime import datetime, time

time_string = crimes['TIME OCC'].value_counts().index[0]
peak_crime_hour = datetime.strptime(time_string, "%H%M").hour

night_time = (crimes['TIME OCC'] > '22:00') & (crimes['DATE OCC'] < '04:00')

peak_night_crime_location = crimes[night_time]['AREA NAME'].value_counts().index[0]

def classify_interval(row):
    if row['Vict Age'] >= 65:
        return "65+"
    elif row['Vict Age'] >= 55:
        return "55-64"
    elif row['Vict Age'] >= 45:
        return "45-54"
    elif row['Vict Age'] >= 35:
        return "35-44"
    elif row['Vict Age'] >= 26:
        return "26-34"
    elif row['Vict Age'] >= 18:
        return "18-25"
    elif row['Vict Age'] > 0:
        return "<18"
    

crimes['AGE CATEGORY'] = crimes.apply(classify_interval, axis=1)

victim_ages = crimes['AGE CATEGORY'].value_counts()

