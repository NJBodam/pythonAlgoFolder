import csv

enrollment = './Data Spreadsheet/enrollments.csv'
engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'

header =[]
with open(engagement_filename, 'r') as f:
    reader = csv.DictReader(f)
    header = next(reader)


print(header)
