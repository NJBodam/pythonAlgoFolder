import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Examine DataFrame
if False:
    print example_df

# Out[1]:
#    value   even  above_three
# a      1  False        False
# b      3  False        False
# c      2   True        False
# d      4   True         True
# e      1  False        False
# f      6   True         True
# g      4   True         True


# Examine groups
if False:
    grouped_data = example_df.groupby('even')   # groupby() returns a GroupBy object where indexes are grouped according to the values of the column 'even'
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print grouped_data.groups   

# Out[2]:
# {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}      # keys are the values of the column 'even' and the values are the indexes of the rows that have that value

# Group by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print grouped_data.groups

# Out[3]:
# {(False, False): ['a', 'b', 'e'], (True, False): ['c'], (True, True): ['d', 'f', 'g']}

# Get sum of each group
if False:
    grouped_data = example_df.groupby('even')
    print grouped_data.sum()

# Out[4]:
#          value  above_three
# even                     
# False      5            0     # 5 = sum of the values of the rows that have 'False' in the column 'even': 0 = sum of the False values in the column 'even' that are above 3
# True      16            3     # 16 = sum of the values of the rows that have 'True' in the column 'even': 3 = sum of the True values in the column 'even' that are above 3


# Limit columns in result
if False:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    print grouped_data.sum()['value']
    
    print '\n' # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    print grouped_data['value'].sum()

# Out[5]:
# even
# False     5
# True     16
# Name: value, dtype: int64
#
# even
# False     5
# True     16
    
filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.

# For setting the index to a column
# grp_data = subway_df.set_index('UNIT')


if True:
    grouped_data = subway_df[:10]
    gdt1 = subway_df[:865].groupby('station')
    gdt2 = subway_df.groupby('conds')
    print(grouped_data.groupby('hour').sum()['ENTRIESn_hourly'])
    print(gdt2.sum()['EXITSn_hourly'])
    rs = subway_df.groupby('hour').sum()['ENTRIESn_hourly']
    
#     plt.plot(subway_df.groupby('day_week').sum()['ENTRIESn_hourly'])
#     plt.plot(rs)
    plt.plot(gdt2.sum()['ENTRIESn_hourly'], linewidth=2, markersize=40)