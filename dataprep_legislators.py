# This script is used to import data from the legislators *.json files and convert them into a combined dataframe.

import json
import pandas as pd
import numpy as np
from datetime import datetime  
from datetime import timedelta 

# Create function to create a Pandas DataFrame from JSON file
def create_dataframe(file):
    # Load data using Python JSON module
    with open(file,'r') as f:
        data = json.loads(f.read())

    # Normalize data
    df = pd.json_normalize(
        data,
        record_path =['terms'],
        meta=[
            ['id', 'bioguide'],
            ['name', 'first'],
            ['name', 'last'],
            ['bio', 'birthday'],
            ['bio', 'gender']
        ],
        errors='ignore' 
    )

    # Convert datetime columns to datetime
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['bio.birthday'] = pd.to_datetime(df['bio.birthday'])

    # Create a mask to isolate relevant columns from data
    mask = ['id.bioguide', 'name.first', 'name.last','start','end','party','state','bio.birthday','bio.gender', 'type']

    # Create a new dataframe with age calculated for each year served in congress
    col_list = ['id', 'first_name', 'last_name', 'party', 'state', 'year', 'age', 'type']
    df_data = []

    ## Loop through rows in original dataframe to compute age for each entry
    for i, row in df[mask].iterrows():
        j = row['start']
        k = row['end']
        while j.year <= k.year:
            age = j.year - row['bio.birthday'].year
            type = row['type']

            ## Set age limits to ensure there aren't incorrect values (25 for house, 30 for senate)
            if type == 'rep':
                age_min = 25
            elif type == 'sen':
                age_min = 30

            if age < age_min:
                age = np.nan
            
            df_data.append([row['id.bioguide'], row['name.first'], row['name.last'], row['party'], row['state'], j.year, age, row['type']])
            j += timedelta(days=365)

    ## Convert list of lists into dataframe and drop duplicates caused by people holding consecutive terms, as well as rows with missing values.
    df = pd.DataFrame(df_data, columns = col_list)
    df = df.drop_duplicates(ignore_index=True).dropna()

    ## Remove years after 2022 (current year) for ongoing terms
    df = df[df['year'] <= 2022]

    return df

# Load and combine historical and current data files
df_historical = create_dataframe('data/legislators-historical.json')
df_current = create_dataframe('data/legislators-current.json')
df_combined = pd.concat([df_historical, df_current], axis=0)
df_combined = df_combined.drop_duplicates(ignore_index=True).dropna()

# Add column to identify first years of terms for each unique id
df_sorted = df_combined.sort_values(by=['id', 'year'])

id_list = set()
first_year = []
for i, row in df_sorted.iterrows():
    if row['id'] in id_list:
        first_year.append('N')
    else:
        id_list.add(row['id'])
        first_year.append('Y')
    
df_sorted['first_year'] = first_year

df_final = df_sorted

# Export to Excel to use with Tableau
df_sorted.to_excel("data/legislators_combined_and_cleaned.xlsx") 
