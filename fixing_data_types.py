from datetime import datetime as dt
from csv_in_python import read_csv as rc


# Takes a date as a string and returns a Python datetime object.

def parse_date(date):
    if date == '':
        return None
    return dt.strptime(date, '%Y-%m-%d')

# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    return int(i)

# clean up the data types in the enrollments table

enrollment = './Data Spreadsheet/enrollments.csv'
engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'

enrollments = rc(enrollment)
daily_engagement = rc(engagement_filename)
project_submissions = rc(submissions_filename)

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

print(enrollments[0])