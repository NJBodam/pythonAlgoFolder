import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

# Change False to True for each block of code to see what it does

# DataFrame creation
if False:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df_1

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print df_2
   
    # output:
    #    A  B
    # 0  0  3
    # 1  1  4
    # 2  2  5

    #    A  B  C
    # 0  0  1  2
    # 1  3  4  5


# Accessing elements
if False:
    print ridership_df.iloc[0]  # first row
    print ridership_df.loc['05-05-11']  # fifth row via index
    print ridership_df['R003']  # first column via column name
    print ridership_df.iloc[1, 3]   # second row, fourth column
    
    # output:
    # R003    0
    # R004    0
    # R005    2
    # R006    5
    # R007    0
    # Name: 05-01-11, dtype: int64
    # R003    1608
    # R004    4802
    # R005    3932
    # R006    4477
    # R007    2705
    # Name: 05-05-11, dtype: int64
    # 05-01-11       0
    # 05-02-11    1478
    # 05-03-11    1613
    # 05-04-11    1560
    # 05-05-11    1608
    # 05-06-11    1576
    # 05-07-11      95
    # 05-08-11       2
    # 05-09-11    1438
    # 05-10-11    1342
    # Name: R003, dtype: int64
    # 2328


# Accessing multiple rows
if False:
    print ridership_df.iloc[1:4]    # second to fourth row

    # output:
    #           R003  R004  R005  R006  R007
    # 05-02-11  1478  3877  3674  2328  2539
    # 05-03-11  1613  4088  3991  6461  2691
    # 05-04-11  1560  3392  3826  4787  2613

    
# Accessing multiple columns
if False:
    print ridership_df[['R003', 'R005']]    # first and third column
    
    # output:
    #           R003  R005
    # 05-01-11     0     2
    # 05-02-11  1478  3674
    # 05-03-11  1613  3991
    # 05-04-11  1560  3826
    # 05-05-11  1608  3932
    # 05-06-11  1576  3909
    # 05-07-11    95   255
    # 05-08-11     2     1
    # 05-09-11  1438  3589
    # 05-10-11  1342  4009


# Pandas axis
if False:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df.sum()
    print df.sum(axis=1)
    print df.values.sum()

    # output:
    # A     3
    # B    12
    # dtype: int64
    # 0    3
    # 1    5
    # 2    7
    # dtype: int64
    # 15


    
def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    overall_mean = None # Replace this with your code
    mean_for_max = None # Replace this with your code

    max_riders = ridership.iloc[0].argmax()
    overall_mean = ridership.values.mean()
    mean_for_max = ridership[max_riders].mean()
    
    return (overall_mean, mean_for_max)