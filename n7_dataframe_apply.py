import pandas as pd

# FIRST USE CASE
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# Change False to True for this block of code to see what it does

# DataFrame apply()
if False:
    def convert_grades_curve(exam_grades):
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    print convert_grades_curve(grades_df['exam1'])
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    print grades_df.apply(convert_grades_curve)
    
def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
     # return df.apply(lambda x: (x - x.mean()) / x.std(ddof=0))

    # def standardize_column(column):
    #     return (column - column.mean()) / column.std(ddof=0)
    
    # for column in df:
    #     df[column] = standardize_column(df[column])
    
    # Shorter version
    grades_df_standardized = grades_df.apply(lambda column: (column - column.mean()) / column.std(ddof=0), axis=0)
    
    print(grades_df_standardized)
    
    # Longer version
    def standardize_column(column):
        return (column - column.mean()) / column.std(ddof=0)
    # apply() does not change the original DataFrame unless you set the inplace parameter to True    
    return df.apply(standardize_column, axis=0)
    

# SECOND USE CASE
df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if True:   
    print df.apply(np.mean)
    print df.apply(np.max)

# Output:
# a     3.0 # mean of column a
# b    30.0 # mean of column b
# c    15.0 # mean of column c
# dtype: float64
# a     5 # max of column a
# b    50 # max of column b
# c    25 # max of column c
# dtype: int64

def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    # My solution
    new_df = df[df < df.apply(np.max)]
    print(new_df.apply(np.max))

    # Alternative solution
    sorted_series = df.sort_values(ascending=False)
    return sorted_series.iloc[1]

# Apply the custom function to each column using apply()
second_largest_values = df.apply(second_largest)
