#Question 7: Investing Data
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.
import csv

enrollment = './Data Spreadsheet/enrollments.csv'
engagement_filename = './Data Spreadsheet/daily_engagement.csv'
submissions_filename = './Data Spreadsheet/project_submissions.csv'
    
def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollment)
daily_engagement = read_csv(engagement_filename)
project_submissions = read_csv(submissions_filename)


enrollment_num_rows = len(enrollments)            # Replace this with your code
enrollment_num_unique_students = set(int(x['account_key']) for x in enrollments)   # Replace this with your code

engagement_num_rows = len(daily_engagement)             # Replace this with your code
engagement_num_unique_students = set(int(x['account_key']) for x in daily_engagement)  # Replace this with your code

submission_num_rows = len(project_submissions)             # Replace this with your code
submission_num_unique_students = set(int(x['account_key']) for x in project_submissions)  # Replace this with your code

enrollment_account_key = sorted(set(int(x['account_key']) for x in enrollments))
engagement_account_key = sorted(set(int(x['account_key']) for x in daily_engagement))

#Students in enrollment but not in engagement
missing_data_points = []

missing_students_rec = []

# for i in enrollment_account_key:
#     if i not in engagement_account_key:
#         missing_data_points.append(i)
#         print(i)
#         i+=1

# count = 0
# while count < 3:
#     print(enrollments[count]['account_key'])
#     count += 1

# for i in enrollments:
#     print(i:3])
    # if i['account_key'] in missing_data_points:
    #     missing_students_rec.append(i)
    #     print(i)
    #     i+=1

# print(missing_students_rec[:5])

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in engagement_num_unique_students \
        and enrollment['join_date'] != enrollment['cancel_date']:
        num_problem_students += 1


udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data