# Read in bank_marketing.csv as a pandas DataFrame.
# Split the data into three DataFrames using information provided about the desired tables as your guide: one with information about the client, another containing campaign data, and a third to store information about economics at the time of the campaign.
# Rename the column "client_id" to "id" in client (leave as-is in the other subsets); "duration" to "contact_duration", "previous" to "previous_campaign_contacts", "y" to "campaign_outcome", "poutcome" to "previous_outcome", and "campaign" to "number_contacts" in campaign; and "euribor3m" to "euribor_three_months" and "nr_employed" to "number_employed" in economics.
# Clean the "education" column, changing "." to "_" and "unknown" to NumPy's null values.
# Remove periods from the "job" column.
# Convert "success" and "failure" in the "previous_outcome" and "campaign_outcome" columns to binary (1 or 0), along with the changing "nonexistent" to NumPy's null values in "previous_outcome".
# Add a column called campaign_id in campaign, where all rows have a value of 1.
# Create a datetime column called last_contact_date, in the format of "year-month-day", where the year is 2022, and the month and day values are taken from the "month" and "day" columns.
# Remove any redundant data that might have been used to create new columns, ensuring the columns in each subset of the data match the table displayed in the notebook.
# Save the three DataFrames to csv files without an index as client.csv, campaign.csv, and economics.csv respectively.
# Create a Python variable called client_table, containing SQL code as a multi-line string to create a table called client using values from client.csv.
# Create a Python variable called campaign_table, containing SQL code as a multi-line string to create a table called campaign using values from campaign.csv.
# Create a Python variable called economics_table, containing SQL code as a multi-line string to create a table called economics using values from economics.csv.
# In client, campaign, and economic, ensure the final line copies the data from their respective csv files using the following template code snippet: \copy table_name from 'file_name.csv' DELIMITER ',' CSV HEADER


# Personal loans are a lucrative revenue stream for banks. The typical interest rate of a two year loan in the United Kingdom is around 10%. This might not sound like a lot, but in September 2022 alone UK consumers borrowed around £1.5 billion, which would mean approximately £300 million in interest generated by banks over two years!

# You have been asked to work with a bank to clean and store the data they collected as part of a recent marketing campaign, which aimed to get customers to take out a personal loan. They plan to conduct more marketing campaigns going forward so would like you to set up a PostgreSQL database to store this campaign's data, designing the schema in a way that would allow data from future campaigns to be easily imported.

# They have supplied you with a csv file called "bank_marketing.csv", which you will need to clean, reformat, and split, in order to save separate files based on the tables you will create. It is recommended to use pandas for these tasks.

# Lastly, you will write the SQL code that the bank can execute to create the tables and populate with the data from the csv files. As the bank are quite strict about their security, you'll save SQL files as multiline string variables that they can then use to create the database on their end.

# You have been asked to design a database that will have three tables:

# client
# column	        data type	description	original column in dataset
# id	            serial	    Client ID - primary key	client_id
# age	            integer	    Client's age in years	age
# job	            text	    Client's type of job	job
# marital	        text	    Client's marital status	marital
# education	        text	    Client's level of education	education
# credit_default	boolean	    Whether the client's credit is in default	credit_default
# housing	        boolean	    Whether the client has an existing housing loan (mortgage)	housing
# loan	            boolean	    Whether the client has an existing personal loan	loan

# campaign
# column	data type	description	original column in dataset
# campaign_id	serial	Campaign ID - primary key	N/A - new column
# client_id	serial	Client ID - references id in the client table	client_id
# number_contacts	integer	Number of contact attempts to the client in the current campaign	campaign
# contact_duration	integer	Last contact duration in seconds	duration
# pdays	integer	Number of days since contact in previous campaign (999 = not previously contacted)	pdays
# previous_campaign_contacts	integer	Number of contact attempts to the client in the previous campaign	previous
# previous_outcome	boolean	Outcome of the previous campaign	poutcome
# campaign_outcome	boolean	Outcome of the current campaign	y
# last_contact_date	date	Last date the client was contacted	A combination of day, month, and the newly created year

# economics
# column	data type	description	original column in dataset
# client_id	serial	Client ID - references id in the client table	client_id
# emp_var_rate	float	Employment variation rate (quarterly indicator)	emp_var_rate
# cons_price_idx	float	Consumer price index (monthly indicator)	cons_price_idx
# euribor_three_months	float	Euro Interbank Offered Rate (euribor) three month rate (daily indicator)	euribor3m
# number_employed	float	Number of employees (quarterly indicator)	nr_employed ~~


# SOLUTION


import pandas as pd
import numpy as np
from datetime import datetime as dt

# Start coding here...

bank_mkt = pd.read_csv('bank_marketing.csv')

client_cols = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'housing', 'loan']

client = bank_mkt[client_cols].rename(columns={'client_id':'id'})

campaign_cols = ['client_id', 'campaign', 'duration', 'pdays', 'previous', 'poutcome', 'y']

campaign = bank_mkt[campaign_cols].rename(columns={"duration":"contact_duration", "previous":"previous_campaign_contacts", "y":"campaign_outcome", "poutcome":"previous_outcome", "campaign":"number_contacts"}).reset_index(names='campaign_id')

economics_cols = ['client_id', 'emp_var_rate', 'cons_price_idx', 'euribor3m', 'nr_employed']
                                                             
economics = bank_mkt[economics_cols].rename(columns={"euribor3m":"euribor_three_months","nr_employed":"number_employed"})

# Cleaning education
client['education'] = client['education'].str.replace('.', '_')
client['education'] = client['education'].replace('unknown', np.nan)
client['job'] = client['job'].str.replace('.', '')

# Converting success and failure
campaign['previous_outcome'] = campaign['previous_outcome'].replace('nonexistent', np.nan)
campaign['previous_outcome'] = campaign['previous_outcome'].replace('success', 1)
campaign['previous_outcome'] = campaign['previous_outcome'].replace('failure', 0)

# Add Column
campaign = campaign.assign(campaign_id=1)

campaign['last_contact_date'] = pd.to_datetime('2022-' + bank_mkt['month'].astype(str) + "-" + bank_mkt['day'].astype(str))

# Save to csv
client.to_csv('client.csv', index=False)
economics.to_csv('economics.csv', index=False)
campaign.to_csv('campaign.csv', index=False)

df = pd.read_csv('campaign.csv')

client_table = """
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    age INT,
    job TEXT,
    marital TEXT,
    education TEXT,
    credit_default BOOLEAN,
    housing BOOLEAN,
    loan BOOLEAN
);
    
\copy client FROM 'client.csv' DELIMITER ',' CSV HEADER;
"""

campaign_table = """
CREATE TABLE campaign (
    campaign_id SERIAL PRIMARY KEY,
    client_id SERIAL REFERENCES client (id),
    number_contacts INT,
    contact_duration INT,
    pdays INT,
    previous_campaign_contacts INT,
    previous_outcome BOOLEAN,
    campaign_outcome BOOLEAN,
    last_contact_date DATE
);

\copy campaign FROM 'campaign.csv' DELIMITER ',' CSV HEADER;
"""

economics_table = """
CREATE TABLE economics (
    client_id SERIAL REFERENCES client (id),
    emp_var_rate FLOAT,
    cons_price_idx FLOAT,
    euribor_three_months FLOAT,
    number_employed FLOAT
);

\copy economics FROM 'economics.csv' DELIMITER ',' CSV HEADER;
"""

# print(economics['cons_price_idx'])