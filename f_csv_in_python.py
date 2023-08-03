### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.
import csv

enrollment = './Data Spreadsheet/enrollments.csv'
engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'

enrollments = []          # Replace this with your code    
daily_engagement = []     # Replace this with your code
project_submissions = []  # Replace this with your code

def read_csv(filename):
    with open(engagement_filename, 'r') as f:
        reader = csv.DictReader(f)
        arr = list(reader)
        if 'acct' in arr:
            arr['account_key'] = arr.pop('acct')
        return arr

enrollments = read_csv(enrollment)
daily_engagement = read_csv(engagement_filename)
project_submissions = read_csv(submissions_filename)

'print(enrollments[0]["account_key"])'

missing_data_points = []

for i in enrollments:
    if i['account_key'] != daily_engagement[i]['account_key']:
        missing_data_points.append(enrollments[i])
        print(enrollments[i]['account_key'])
        i+=1

