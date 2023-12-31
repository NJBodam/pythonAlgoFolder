import pandas as pd

# Examples of vectorized operations on DataFrames:
# Change False to True for each block of code to see what it does

# Adding DataFrames with the column names
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    print(df1 + df2)
    
# Adding DataFrames with overlapping column names 
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    print(df1 + df2)

# Adding DataFrames with overlapping row indexes
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    print(df1 + df2)

# --- Quiz ---
# Cumulative entries and exits for one station for a few hours.
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    '''
    
    entries_and_exits = entries_and_exits - entries_and_exits.shift(1)  # shift(1) means shift down 1 row
    # Alternative: entries_and_exits =
    entries_and_exits.diff()

    print(entries_and_exits)
    entries_and_exits.iloc[0] = 0
    return entries_and_exits

print(get_hourly_entries_and_exits(entries_and_exits))

# Output:
#    ENTRIESn  EXITSn
# 0       NaN     NaN
# 1      23.0     8.0
# 2      18.0    18.0
# 3      71.0    54.0
# 4     170.0    44.0
# 5     214.0    42.0
# 6      87.0    11.0
# 7      10.0     3.0
# 8      36.0    89.0
# 9     153.0   333.0
#     ENTRIESn  EXITSn
# 0        0.0     0.0
# 1       23.0     8.0
# 2       18.0    18.0
# 3       71.0    54.0
# 4      170.0    44.0
# 5      214.0    42.0
# 6       87.0    11.0
# 7       10.0     3.0
# 8       36.0    89.0
# 9      153.0   333.0
