# Start by assessing global demand for working out. To do this, call one of the helper functions to load the workout.csv file into a DataFrame, and the function will also plot the data over time; you'll see that interest in workouts appears to be seasonal.
# Use pandas and other coding methods on the DataFrame you created to assess the month in which demand for fitness is highest across the world, on average. Create a string variable month_str containing the month with the highest interest from this workout_by_month, in the format of "yyyy-mm-dd."
# Next, load the file called three_keywords.csv using the same function as before, into a DataFrame. This file tracks global interest in three keywords. After visually assessing the plot, create a variable called current which equals the keyword string value that you can see generated the most interest from 2022 to 2023. Create a second variable, peak_covid, indicating which keyword string value that you can see generated the most interest during 2020.
# You'll now disaggregate global demand in the "workout" keyword by region to find the top 25 countries with the highest interest in workouts. Read workout_global.csv into a DataFrame, using the appropriate function provided for loading geographic data. Note that the helper function sorts the values in the DataFrame it returns. Have a look at the plot. Use pandas code to create a variable top_country with a string value for the name of the country with the highest interest in workouts.
# Use the appropriate helper function with the file geo_three_keywords.csv to load its geographic data, and save it as geo_categories. This time, however, you are using multiple keywords, so you'll need to change an argument. You saw in the previous plot that many countries from the Middle East and South Asia are in the top 25 countries with interest in workouts, including "Philippines", "Singapore", "United Arab Emirates," "Qatar," "Kuwait," "Lebanon," "Malaysia," "Sri Lanka," "India," and "Pakistan." Filter geo_categories to return only these countries and save this as a DataFrame MESA.
# Next you want to assess the split of interest in these three keywords in these MESA countries by each country and category. See if you can create a table of this data using some pandas code, so you can visually identify the country with the highest interest in home workouts, and save it as a string to a variable top_home_workout_country. If you can't see all the data in your visualization, minimize the left sidebar until you can. Not all countries in your list will be visible; this is normal when Google does not have enough data on searches.
# You can see in the data that the country you just identified as having the highest interest in home workouts has little interest in home gyms, so you'll look at YouTube keyword searches next. Use a helper function to load the two files data/yoga_zumba_sng.csv and data/yoga_zumba_phl.csv, allowing you to compare data for Singapore and Philippines respectively. Create a list, pilot_content, which contains the top two media types (not including "workout") that you see in the plots are worth piloting in digital form in these countries.# STARTER CODE - PLEASE DO NOT EDIT ANY CODE IN THIS CELL

# Start your coding here ....
df_workout = read_file('data/workout.csv')
df_three_keywords = read_file('data/three_keywords.csv')
df_workout_global = read_geo('data/workout_global.csv')
geo_categories = read_geo('data/geo_three_keywords.csv', True)

sng = read_file('data/yoga_zumba_sng.csv').sort_values('interest', ascending=False)

phl = read_file('data/yoga_zumba_phl.csv').sort_values('interest', ascending=False)


MESA_CAT = ["Philippines", "Singapore", "United Arab Emirates," "Qatar," "Kuwait," "Lebanon," "Malaysia," "Sri Lanka," "India,", "Pakistan."]

month_str = df_workout.sort_values('interest', ascending=False).iloc[0,0].replace(day=1).strftime('%Y-%m-%d')

current = df_three_keywords[df_three_keywords['week'] > '2022-01-01'].sort_values('interest', ascending=False).iloc[0,1].split(':')[0]

peak_covid = df_three_keywords[df_three_keywords['week'].dt.year == 2020].sort_values('interest', ascending=False).iloc[0,1].split(':')[0]

top_country = df_workout_global.iloc[0,0]

MESA = geo_categories[geo_categories['country'].isin(MESA_CAT)]

top_home_workout_country = MESA.iloc[0,0]

media_sng = sng[~sng['region'].isin(['workout: (Singapore)'])].iloc[0,1].split(':')[0]

media_phl = phl[~phl['region'].isin(['workout: (Philippines)'])].iloc[0,1].split(':')[0]

pilot_content = [media_sng, media_phl]




