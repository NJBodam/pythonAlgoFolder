# What's in an Avocado Toast: A Supply Chain Analysis
# You're in London, making an avocado toast, a quick-to-make dish that has soared in popularity on breakfast menus since the 2010s. A simple smashed avocado toast can be made with five ingredients: one ripe avocado, half a lemon, a big pinch of salt flakes, two slices of sourdough bread and a good drizzle of extra virgin olive oil. It's no small feat that most of these ingredients are readily available in grocery stores.

# In this project, you'll conduct a supply chain analysis of three of these ingredients used in an avocado toast, utilizing the Open Food Facts database. This database contains extensive, openly-sourced information on various foods, including their origins. Through this analysis, you will gain an in-depth understanding of the complex supply chain involved in producing a single dish.

# Three pairs of files are provided in the data folder:

# A CSV file for each ingredient, such as avocado.csv, with data about each food item and countries of origin
# A TXT file for each ingredient, such as relevant_avocado_categories, containing only the category tags of interest for that food.
# Here are some other key points about these files:

# Some of the rows of data in each of the three CSV files do not contain relevant data for your investigation. In each dataset, you will need to filter out rows with irrelevant data, based on values in the categories_tags column. Examples of categories are, fruits, vegetables, and fruit-based oils. Filter the DataFrame to include only rows where categories_tags contains one of the tags in the relevant categories for that ingredient.
# Each row of data usually has multiple categories tags in the categories_tags column.
# There is a column in each CSV file called origins_tags with strings for country of origin of that item.
# After completing this project, you'll be armed with a list of ingredients and their countries of origin, and be well-positioned to launch into other analyses that explore how long, on average, these ingredients spend at sea.

# SOLUTION

import pandas as pd
import numpy as np

# Begin coding here ...

# List of relevant columns to be analyzed
col = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']

# Read csv from a tab seperated csv file
avo = pd.read_csv('data/avocado.csv', sep='\t')[col].dropna(subset = 'categories_tags')
oyl = pd.read_csv('data/olive_oil.csv', sep='\t')[col].dropna(subset = 'categories_tags')
sou = pd.read_csv('data/sourdough.csv', sep='\t')[col].dropna(subset = 'categories_tags')

# List of relevant category tags of interest for ingredients 
rel_avo_cat = read_txt('data/relevant_avocado_categories.txt')
rel_oli_cat = read_txt('data/relevant_olive_oil_categories.txt')
rel_sou_cat = read_txt('data/relevant_sourdough_categories.txt')

# Function for sorting data based on the relevant category of interest
def relevant_data_maker(data, relevant_category):
    data['category_relevant'] = data['categories_tags'].str.split(',').apply(lambda x: any(i for i in x if i in relevant_category))
    return data[data['category_relevant']]

# Applying function
avo = relevant_data_maker(avo, rel_avo_cat)
oyl = relevant_data_maker(oyl, rel_oli_cat)
sou = relevant_data_maker(sou, rel_sou_cat)

# Filtering by the United Kingdom
avo_uk = avo[avo['countries'] == 'United Kingdom']
oyl_uk = oyl[oyl['countries'] == 'United Kingdom']
sou_uk = sou[sou['countries'] == 'United Kingdom']

# Function for cleaning, filtering and outputing result

def clean_filter_result(series):
    items = ",".join(series['origins_tags'].dropna()).split(',')
    clean_val = lambda val: val.split(':')[1]
    new_items = list(map(clean_val, items))
    return pd.DataFrame(new_items).value_counts().idxmax()[0]


top_avocado_origin = clean_filter_result(avo_uk).upper()
top_olive_oil_origin = clean_filter_result(oyl_uk).upper()
top_sourdough_origin = clean_filter_result(sou_uk).replace('-', ' ').upper()

