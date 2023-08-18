import pandas as pd

# Adding using +
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s

    #Output:
#     0   1    2    3
# 0  10  50   90  130
# 1  20  60  100  140
# 2  30  70  110  150
# 3  40  80  120  160

#     0   1    2    3
# 0  11  52   93  134
# 1  21  62  103  144
# 2  31  72  113  154
# 3  41  82  123  164

    
# Adding with axis='index'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='index')
    # The functions sub(), mul(), and div() work similarly to add()

   #Output:
#     0   1    2    3
# 0  10  50   90  130
# 1  20  60  100  140
# 2  30  70  110  150
# 3  40  80  120  160

#     0   1    2    3
# 0  11  51   91  131
# 1  22  62  102  142
# 2  33  73  113  153
# 3  44  84  124  164
    
# Adding with axis='columns'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='columns')
    # The functions sub(), mul(), and div() work similarly to add()

    #Output:
    # 0   1    2    3
# 0  10  50   90  130
# 1  20  60  100  140
# 2  30  70  110  150
# 3  40  80  120  160

#     0   1    2    3
# 0  11  52   93  134
# 1  21  62  103  144
# 2  31  72  113  154
# 3  41  82  123  164
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''

    mean = df.mean(axis='index')
    std = df.std(axis='index', ddof=0)
    return (df.sub(mean)).div(std)

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''

    mean = df.mean(axis='columns')
    std = df.std(axis='columns', ddof=0)
    return (df.sub(mean, axis='index')).div(std, axis='index')  # this takes the mean of each row and subtracts it from each element in the row, then divides by the standard deviation of each row

print(standardize(grades_df))
print(standardize_rows(grades_df))

#Output:
#           exam1     exam2
# Andre   -2.315341 -2.304599
# Barry    0.220191  0.386400
# Chris    0.020017 -0.096600
# Dan     -0.180156 -0.096600
# Emilio   0.753987  0.662400
# Fred    -0.513779 -0.441600
# Greta    0.887436  1.490400
# Humbert -0.847401 -0.786600
# Ivan     1.354508  1.007400
# James    0.620538  0.179400

#           exam1     exam2
# Andre      1.0   -1.0
# Barry      1.0   -1.0
# Chris      1.0   -1.0
# Dan        1.0   -1.0
# Emilio     1.0   -1.0
# Fred       1.0   -1.0
# Greta      1.0   -1.0
# Humbert    1.0   -1.0
# Ivan       1.0   -1.0
# James      1.0   -1.0