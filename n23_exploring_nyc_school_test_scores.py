# Create a pandas DataFrame called best_math_schools containing the "school_name" and "average_math" score for all schools where the results are at least 80% of the maximum possible score, sorted by "average_math" in descending order.
# Identify the top 10 performing schools based on scores across the three SAT sections, storing as a pandas DataFrame called top_10_schools containing the school name and a column named "total_SAT", with results sorted by total_SAT in descending order.
# Locate the NYC borough with the largest standard deviation for "total_SAT", storing as a DataFrame called largest_std_dev with "borough" as the index and three columns: "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT", and "std_SAT" for the standard deviation of "total_SAT". Round all numeric values to two decimal places.

# Re-run this cell 
import pandas as pd
import numpy as np

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

pass_mark = 640


# def num_schools(x):
#     return x.size
    
# def average_SAT(x):
#     y = np.mean(x)
#     return round(y, 2)

# def std_SAT(x):
#     y = np.std(x)
#     return round(y, 2)

best_math_schools = schools[schools["average_math"] >= pass_mark][["school_name", "average_math"]].sort_values("average_math", ascending=False)

# best_math_schools = schools.sort_values("average_math", ascending=False).loc[schools.average_math >= pass_mark, ["school_name", "average_math"]]

# Calculate total_SAT per school
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# schools["total_SAT"] = schools[["average_math","average_reading","average_writing"]].sum(axis=1)

# top_10_schools = schools[["school_name","total_SAT"]].sort_values("total_SAT", ascending=False).head(10)


# Who are the top 10 performing schools?
top_10_schools = schools.groupby("school_name", as_index=False)["total_SAT"].mean().sort_values("total_SAT", ascending=False).head(10)

largest_std_dev2 = df.groupby("borough").agg(num_schools=("total_SAT","count"), average_SAT=("total_SAT","mean"), std_SAT=("total_SAT","std")).round(2).reset_index(names="borough")

largest_std_dev2 = largest_std_dev.sort_values(by="std_SAT", ascending=False).head(1)

largest_std_dev1 = schools.groupby("borough")["total_SAT"].agg([num_schools, average_SAT, std_SAT]).sort_values("std_SAT", ascending=False).head(1)

# Which NYC borough has the highest standard deviation for total_SAT?
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filter for max std and reset index so borough is a column
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

print(largest_std_dev1)

