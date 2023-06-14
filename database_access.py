import sqlite3
import pandas as pd

DATABASE_PATH_2021 = 'home_depot_data_2021.db'
CSV_PATH_2021 = 'home_depot_data_2021.csv'

DATABASE_PATH_2023 = 'home_depot_data_2023.db'
CSV_PATH_2023 = 'home_depot_data_2023.csv'

# Code to populate database
# Note: Only needs to be ran once.
# Step 1: create 'home_depot_data.db' in directory
# Step 2: uncomment code under "Web crawled 2021 data" or "Web crawled 2023 data"
# Step 3: run python database_access.py in terminal 
# Step 4: recomment this code to prevent errors

# conn = sqlite3.connect(DATABASE_PATH_2021)
# c = conn.cursor()

# Web crawled 2021 data
# c.execute('''CREATE TABLE home_depot_data_2021 (url TEXT, name TEXT, description TEXT, brand TEXT, price REAL,
#     currency TEXT, breadcrumbs TEXT, overview TEXT, specifications TEXT)''')

# Web crawled 2023 data
# c.execute('''CREATE TABLE home_depot_data_2023 (details TEXT, seller TEXT, title TEXT, url TEXT)''')

# load to Pandas DataFrame
# home_depot_data = pd.read_csv(CSV_PATH_2021)
# write data to a sqlite table
# home_depot_data.to_sql('home_depot_data_2021', conn, if_exists='append', index=False)

####################################################################################

def run_query(query):
    con = sqlite3.connect(DATABASE_PATH_2021)
    try:
        response = pd.read_sql_query(query, con)
        return response
    finally:
        con.close()

def sql_query(query):
    return run_query(query).to_markdown()
