import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Standardize each group
if False:
    def standardize(xs):
        return (xs - xs.mean()) / xs.std()
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(standardize)

# Out[5]:           # the values of the column 'value' are standardized according to the values of the column 'even'
# a   -0.577350
# b    1.154701
# c   -1.224745
# d    0.000000
# e   -0.577350
# f    1.224745
# g    0.000000 
# Name: value, dtype: float64
 
# Find second largest value in each group
if False:
    def second_largest(xs):
        sorted_xs = xs.sort(inplace=False, ascending=False)
        return sorted_xs.iloc[1]
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(second_largest)

# Out[6]:        # the second largest value of the column 'value' is returned according to the values of the column 'even' after sorting the values of the column 'value' in descending order
# even
# False    1
# True     4
# Name: value, dtype: int64



# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    
    Hint: Take a look at the `get_hourly_entries_and_exits()` function
    you wrote in a previous quiz, DataFrame Vectorized Operations. If
    you copy it here and rename it, you can use it and the `.apply()`
    function to help solve this problem.
    '''

    # The thought process:
    # 1. Group by 'UNIT'
    # 2. For each group, get the hourly entries and exits


    # My solution

    def diff(x):
        return x.diff()
    # OR
    def get_hourly_entries_and_exits_for_group(entries_and_exits):
        return entries_and_exits - entries_and_exits.shift(1)
    
    return entries_and_exits.groupby('UNIT')[['ENTRIESn', 'EXITSn']].apply(get_hourly_entries_and_exits_for_group)

# Outpout:          
#    ENTRIESn  EXITSn
# 0       NaN     NaN
# 1       NaN     NaN
# 2      23.0     8.0       # 3144335 - 3144312 = 23, 1088159 - 1088151 = 8 for UNIT R051
# 3      14.0     8.0       # 8936658 - 8936644 = 14, 13755393 - 13755385 = 8 for UNIT R079
# 4      18.0    18.0       # 3144353 - 3144335 = 18, 1088177 - 1088159 = 18 for UNIT R051
# 5      29.0   205.0       # 8936687 - 8936658 = 29, 13755598 - 13755393 = 205 for UNIT R079
# 6      71.0    54.0
# 7     132.0   593.0
# 8     170.0    44.0