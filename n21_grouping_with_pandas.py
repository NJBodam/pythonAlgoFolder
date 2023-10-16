# Grouping data with pandas
# The output of a data pipeline is typically a "modeled" dataset. This dataset provides data consumers easy access to information, without having to perform much manipulation. Grouping data with pandas helps to build modeled datasets,

# pandas has been imported as pd, and the raw_testing_scores DataFrame contains data in the following form:

#               street_address       city  math_score  reading_score  writing_score
# 01M539   111 Columbia Street  Manhattan       657.0          601.0          601.0
# 02M294      350 Grand Street  Manhattan       395.0          411.0          387.0
# 02M308      350 Grand Street  Manhattan       418.0          428.0          415.0
# Instructions
# 100 XP
# Use .loc[] to only keep the "city", "math_score", "reading_score", and "writing_score" columns.
# Group the DataFrame by the "city" column, and find the mean of each city's math, reading, and writing scores.
# Use the transform() function to create a grouped DataFrame.

def transform(raw_data):
	# Use .loc[] to only return the needed columns
	raw_data = raw_data.loc[:, ['city', 'math_score', 'reading_score', 'writing_score']]
	
    # Group the data by city, return the grouped DataFrame
	grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
	return grouped_data

# Transform the data, print the head of the DataFrame
grouped_testing_scores = transform(raw_testing_scores)
print(grouped_testing_scores.head())

