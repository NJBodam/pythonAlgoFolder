#Question 7: Investing Data
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.
import csv

enrollment = './Data Spreadsheet/enrollments.csv'
engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'
    
def read_csv(filename):
    with open(engagement_filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollment)
daily_engagement = read_csv(engagement_filename)
project_submissions = read_csv(submissions_filename)



enrollment_num_rows = len(enrollments)            # Replace this with your code
enrollment_num_unique_students = len(set(int(x['account_key']) for x in enrollments))   # Replace this with your code

engagement_num_rows = len(daily_engagement)             # Replace this with your code
engagement_num_unique_students = len(set(int(x['acct']) for x in daily_engagement))  # Replace this with your code

submission_num_rows = len(project_submissions)             # Replace this with your code
submission_num_unique_students = len(set(int(x['account_key']) for x in project_submissions))  # Replace this with your code

