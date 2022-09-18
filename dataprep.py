import json
import pandas as pd
from datetime import datetime  
from datetime import timedelta 

# load data using Python JSON module
with open('data/legislators-current.json','r') as f:
    data = json.loads(f.read())

# Normalizing data
df_original = pd.json_normalize(
    data,
    record_path =['terms'],
    meta=[
        ['name', 'first'],
        ['name', 'last'],
        ['bio', 'birthday'],
        ['bio', 'gender']
    ]
)

# Convert datetime columns to datetime
df_original['start'] = pd.to_datetime(df_original['start'])
df_original['end'] = pd.to_datetime(df_original['end'])
df_original['bio.birthday'] = pd.to_datetime(df_original['bio.birthday'])

# Create a mask to isolate relevant columns from data
mask = ['name.first', 'name.last','start','end','party','state','bio.birthday','bio.gender']

# Create a new dataframe with age calculated for each year served in congress
col_list = ['first_name', 'last_name', 'party', 'state', 'year', 'age']
df_data = []

## Loop through rows in original dataframe to compute age for each entry
for i, row in df_original[mask].iterrows():
    i = row['start']
    j = row['end']
    while i.year <= j.year:
        df_data.append([row['name.first'], row['name.last'], row['party'], row['state'], i.year, (i.year - row['bio.birthday'].year)])
        i += timedelta(days=365)

## Convert list of lists into dataframe and drop duplicates caused by people holding consecutive terms.
df = pd.DataFrame(df_data, columns = col_list)
df = df.drop_duplicates(ignore_index=True)

## Checks to verify no null values and that the df was properly produced.
# print(df.isnull().sum())
# print(df.head(10))