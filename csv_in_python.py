### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.
import csv

engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'
    
daily_engagement = []     # Replace this with your code
project_submissions = []  # Replace this with your code

with open(engagement_filename, 'r') as f:
    reader = csv.DictReader(f)
    daily_engagement = list(reader)

with open(submissions_filename, 'r') as f:
    reader = csv.DictReader(f)
    project_submissions = list(reader)


print(daily_engagement[:5])