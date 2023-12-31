# Sports clothing and athleisure attire is a huge industry, worth approximately $193 billion in 2021 with a strong growth forecast over the next decade!

# In this notebook, you will undertake the role of a product analyst for an online sports clothing company. The company is specifically interested in how it can improve revenue. You will dive into product data such as pricing, reviews, descriptions, and ratings, as well as revenue and website traffic, to produce recommendations for its marketing and sales teams.

# You've been provided with four datasets to investigate:

# brands.csv
# Columns	Description
# product_id	Unique product identifier
# brand	Brand of the product
# finance.csv
# Columns	Description
# product_id	Unique product identifier
# listing_price	Original price of the product
# sale_price	Discounted price of the product
# discount	Discount off the listing price, as a decimal
# revenue	Revenue generated by the product
# info.csv
# Columns	Description
# product_name	Name of the product
# product_id	Unique product identifier
# description	Description of the product
# reviews.csv
# Columns	Description
# product_id	Unique product identifier
# rating	Average product rating
# reviews	Number of reviews for the product

# The company has asked you to answer the following questions:

# What is the volume of products and average revenue for Adidas and Nike products based on listing price quartiles?

# Label products priced up to quartile one as "Budget", quartile two as "Average", quartile three as "Expensive", and quartile four as "Elite".
# Store as a pandas DataFrame called adidas_vs_nike containing the following columns: "brand", "price_label", "num_products", and "mean_revenue". All numeric values should be rounded to two decimal places.

# Do any differences exist between the word count of a product's description and its mean rating?

# Split product description length into bins of 100 words and calculate the average rating and number of reviews.
# Store the results as a pandas DataFrame called description_lengths containing the following columns: "description_length", "mean_rating", "num_reviews", again rounding numeric values to two decimal places.

# How does the volume of products and median revenue vary between clothing and footwear?

# Search "description" for "shoe*", "trainer*", or "foot*" and use the results to calculate the number of footwear products versus clothing products sold by the company and the median revenue for each of the two product types.
# Create a pandas DataFrame called product_types containing the following columns: "num_clothing_products", "median_clothing_revenue", "num_footwear_products", "median_footwear_revenue".
# In order to answer the above questions, you'll need to start by reading in the data, merging them together, and removing null values.
import pandas as pd

brands = pd.read_csv("brands.csv") 
finance = pd.read_csv("finance.csv")
info = pd.read_csv("info.csv")
reviews = pd.read_csv("reviews.csv")

# Start coding here...
print(brands.head())


finance_brands = finance.merge(brands, on='product_id').merge(info, on='product_id')

finance_brands = finance_brands.merge(reviews, on='product_id').dropna()


finance_brands['price_label'] = pd.qcut(finance_brands['listing_price'], [0, 0.25, 0.5, 0.75, 1], labels=['Budget','Average', 'Expensive', 'Elite'])


adidas_vs_nike = finance_brands.groupby(['brand','price_label'], as_index=False).agg(num_products=("product_id","count"), mean_revenue=("revenue","mean")).round(2)

finance_brands['description_length'] = finance_brands['description'].str.len()
max_length = finance_brands['description_length'].max()

limits = list(range(0, 800, 100))

labels = [str(i) for i in limits][1:]


finance_brands["description_length"] = pd.cut(finance_brands["description_length"], bins=limits, labels=labels)

description_lengths = finance_brands.groupby(['description_length'], as_index=False).agg(mean_rating=("rating","mean"), num_reviews=("reviews","count")).round(2)


finance_brands['product_types'] = finance_brands["description"].str.contains("shoe*|trainer*|foot")

footwear = finance_brands[finance_brands['product_types']]

clothing = finance_brands[~finance_brands['product_types']]

clothing.dropna(inplace=True)

product_types = pd.DataFrame({"num_clothing_products": len(clothing), 
                              "median_clothing_revenue": clothing["revenue"].median(), 
                              "num_footwear_products": len(footwear), 
                              "median_footwear_revenue": footwear["revenue"].median()}, 
                              index=[0])



