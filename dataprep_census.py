# This script is used to import data from the census *.csv files and convert them into a combined dataframe.

import pandas as pd
import re
import glob

# Build a list of all csv files.
files = glob.glob('data/*.csv')
year_list = []
age_list = []

# Iterate over each csv file, pulling in the median age for the year.
# Following data exploration, the year is located in the first row, third column of each file .iloc[0,2].
for file in files:
    year = re.search(r'20..', file).group(0)
    year_list.append(int(year))
    df = pd.read_csv(file, skiprows=1)
    age = df.iloc[0,2]
    age_list.append(age)

# Create DataFrame with year and median age, and sort by year.
df = pd.DataFrame()
df['year'] = year_list
df['median_age'] = age_list
df_final = df.sort_values(by=['year']).reset_index(drop=True)

# Export to Excel to use with Tableau
df_final.to_excel("data/census.xlsx") 