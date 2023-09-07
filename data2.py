import pandas as pd
import pycountry
df = pd.read_csv("WEO2.csv", encoding='ISO-8859-1')

import pycountry
import pandas as pd

# Sample DataFrame for demonstration
# Let's assume you've read your data into df and it has a column named 'ISO'
# df = pd.read_csv('your_file.csv')

def get_country_name(country_code):
    try:
        return pycountry.countries.get(alpha_3=country_code).name
    except (AttributeError, LookupError):   # Handling both AttributeError and LookupError
        # In case a country isn't found, we'll return a placeholder
        return "Unknown"


# Applying the function to the 'ISO' column to transform it
df['Country Name'] = df['ISO'].apply(get_country_name)

#print(df.head())  # Printing the top rows for verification
#print(df['ISO'].unique())
#print(get_country_name('USA'))  # should print "United States"
df['Country Name'] = df['ISO'].apply(get_country_name)
#print(df.head())  # print the first few rows to check if transformation worked
#df.to_csv('/Users/kailinzhang/PycharmProjects/data1/modified_data.csv', index=False)
# Define the columns you want to drop directly
columns_to_drop = ["WEO Country Code", "ISO", "WEO Subject Code", "Scale"]

# Add the range of columns from 1980 to 2012
columns_to_drop += [str(year) for year in range(1980, 2013)]

# Drop the specified columns
df.drop(columns=columns_to_drop, inplace=True)
#df.to_csv('/Users/kailinzhang/PycharmProjects/data1/modified_data.csv', index=False)
df = df.drop(columns=['Country Name', 'Estimates Start After'])
#df.to_csv('modified_file.csv', index=False)
#print(df.columns)
#df.to_csv('modified_file.csv', index=False)
df = df[df['Subject Notes'] == "Annual percentages of average consumer prices are year-on-year changes."]
#df.to_csv('modified_file.csv', index=False)
df.drop(columns=['Country/Series-specific Notes'], inplace=True)
df.dropna(how='all', inplace=True)
#df.to_csv('modified_file.csv', index=False)
# Example: dropping rows where columns 'A' and 'B' are missing
df.dropna(subset=['2013', '2014'], inplace=True)
#df.to_csv('modified_file.csv', index=False)
# Convert '2013' and '2018' columns to float
df['2013'] = df['2013'].astype(float)
df['2018'] = df['2018'].astype(float)

# Calculate the growth rate
df['Inflation Growth 2013-2018 (%)'] = ((df['2018'] - df['2013']) / df['2013']) * 100
#df.to_csv('modified_file.csv', index=False)
df['Inflation Growth 2013-2018 (%)'] = df['Inflation Growth 2013-2018 (%)'].round(2)
df.to_csv('modified_file.csv', index=False)
