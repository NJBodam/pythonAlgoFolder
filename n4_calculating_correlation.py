import pandas as pd

filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''

    # Easy way
    pearson_corr = x.corr(y, method='pearson')
    
    # Hard way

    # Calculate means
    mean_x = x.mean()
    mean_y = y.mean()

    # Calculate deviations from the mean
    deviations_x = x - mean_x
    deviations_y = y - mean_y

    # Calculate sum of products of deviations
    sum_product_deviations = np.sum(deviations_x * deviations_y)

    # Calculate sum of squares of deviations
    sum_squared_deviations_x = np.sum(deviations_x**2)
    sum_squared_deviations_y = np.sum(deviations_y**2)

    # Calculate correlation coefficient
    correlation_coefficient = sum_product_deviations / np.sqrt(sum_squared_deviations_x * sum_squared_deviations_y)

    print(correlation_coefficient)

    return None

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print correlation(entries, rain)
print correlation(entries, temp)
print correlation(rain, temp)

print correlation(entries, cum_entries)


# Your function did not return the correct answer for the following test case:

# x = pd.Series([1, 2, 3, 4]) y = pd.Series([10, 11, 12, 13])

# Your code returned None. The expected answer was 1.0.