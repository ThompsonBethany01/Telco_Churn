import pandas as pd

# Function to prepare the data, i.e. deal with outliers/missing values, create dummy vars, etc.
def prep_telco_df(telco_churn_df):
    if telco_churn_df.duplicated().sum() == 0:
        print('No duplicates found.')
    else:
        teclo_churn_df = telco_churn_df[~telco_churn_df.duplicated()]
        print('Duplicates removed.')

    # Creating dummy variables of gender
    # Creates a data frame of gender dummy variables, male == 1 and female == 0
    df_dummies = pd.get_dummies(telco_churn_df.gender, drop_first=True)

    # Add to the original df
    df = pd.concat([telco_churn_df, df_dummies],axis=1)

    # Drop the column, we do not need the string version of gender
    df = df.drop('gender', axis=1)
    print('Dummy variables for gender created as "male".')

    # Several columns are being represented by yes and no
    # Going to replace Yes and No for any columns whose only value is Yes or No
    # Ex: multiple lines includes yes, no, and no phone service
    # Yes == 1, No == 0
    df['partner'] = df['partner'].replace({'No': 0, 'Yes': 1})
    df['dependents'] = df['dependents'].replace({'No': 0, 'Yes': 1})
    df['phone_service'] = df['phone_service'].replace({'No': 0, 'Yes': 1})
    df['paperless_billing'] = df['paperless_billing'].replace({'No': 0, 'Yes': 1})
    df['churn'] = df['churn'].replace({'No': 0, 'Yes': 1})

    print('Yes/No column values changed to boolean, 0 as no and 1 as yes')

    # Prepping tenure columns
    # Renaming tenure to tenure_months before creating a tenure_years column
    df = df.rename(columns = {'tenure':'tenure_months'})

    # Creating a new feature, tenure in years, by dividing tenure in months by 12
    df['tenure_years'] = round(df.tenure_months / 12, 2)

    print('Added feature for tenure in years.')

    # Converting total_charges to a float
    # First, have to convert all '' values with 0
    df['total_charges'] = df.total_charges.where((df.tenure_months != 0),0)
    # Now we can convert to float
    df = df.astype({'total_charges':'float64'})

    print('Converted total_charges to float for easier manipulation.')
    print('Data prep complete.')

    return df

# Function to split the data into train, validate, and test
def train_test_validate(telco_churn_df):
    # Import to use split function, can only split two at a time
    from sklearn.model_selection import train_test_split

    # Frist, split into train + validate together and test by itself
    # Test will be about %10 of the data, train + validate is %70 for now
    # Set random_state so we can reproduce the same 'random' data
    train_validate, test = train_test_split(telco_churn_df, test_size = .10, random_state = 123)

    # Second, we plit train + validate into their seperate variables
    # Train will be about %70 of the data, Validate will be about %20 of the data
    train, validate = train_test_split(train_validate, test_size = .20, random_state = 123)

    # These two print functions allow us to ensure the date is properly split
    # Will print the shape of each variable when running the function
    print("train shape: ", train.shape, ", validate shape: ", validate.shape, ", test shape: ", test.shape)

    # Will print the shape of eachvariable as a percentage of the total data set
    # Varialbe to hold the sum of all rows (total observations in the data)
    total = telco_churn_df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
            ", validate percent: ", round(((validate.shape[0])/total),2) * 100, 
            ", test percent: ", round(((test.shape[0])/total),2) * 100)

    return train, validate, test