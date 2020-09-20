# Data is aquired from the company SQL Database, login credentials are required

# Imports used in function
# OS allows us to check if the data is already stored on our computer
import os

# Pandas reads the data into the variable
import pandas as pd

# Holds login credintails for SQL Database in a seperate file not added to GitHub
# env should only be stored locally on your computer
# Add to your .gitignore file to ensure credentials not compromised by uploading online
from env import host, username, password

# Function uses Login credentials to create a connection to the company SQL database
# NOTE: BE SURE NOT TO ADD YOUR CREDENTIALS TO GITHUB WHEN RECREATING THE PROJECT
def get_db_url(db_name):

    # Creates the url and the function returns this url
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return (url)

# Function connects to the SQL database to store the data in a variable which can be used throughout the project
# Saves the data as a .csv file, returns as a pandas data frame
def get_churn_data():

    # data_name allows the function to work no matter what a user might have saved their file name as
    # First, we check if the data is already stored in the computer
    # First conditional runs if the data is not already stored in the computer
    if os.path.isfile('telco_churn.csv') == False:

        # Querry selects the whole dataframe, joing each table on their foriegn keys
        # We will have double columns on the foriegn keys because they are joined together
        sql_querry = '''
                        SELECT *
                        FROM customers AS c
                        JOIN contract_types AS ct ON c.contract_type_id = ct.contract_type_id
                        JOIN payment_types AS pt ON c.payment_type_id = pt.payment_type_id
                        JOIN internet_service_types AS ist ON c.internet_service_type_id = ist.internet_service_type_id;
                    '''

        # Connecting to the data base and using the querry above to select the data
        # the pandas read_sql function reads the query into a DataFrame
        df = pd.read_sql(sql_querry, get_db_url('telco_churn'))

        # We do not need the duplicate columns from the foriegn tables being joined
        # df.columns.duplicated() returns a boolean array, True for a duplicate or False if it is unique up to that point
        # Use ~ to flip the booleans and return the df as any columns that are not duplicated
        # df.loc accesses a group of rows and columns by label(s) or a boolean array
        df = df.loc[:,~df.columns.duplicated()]

        # The pandas to_csv function writes the data frame to a csv file
        # This allows data to be stored locally for quicker exploration and manipulation
        df.to_csv('telco_churn.csv')

    # This conditional runs if the data has already been saved as a csv (if the function has already been run on your computer)
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df = pd.read_csv('telco_churn.csv', index_col=0)

    return df

    # Code to remove duplicates of a df found at:
    # https://www.interviewqs.com/ddi_code_snippets/remove_duplicate_cols