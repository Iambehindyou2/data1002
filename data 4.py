import pandas as pd

df = pd.read_csv("cost.csv", encoding='ISO-8859-1', skiprows=2)
#print(df.head())
# Setup the list of columns to drop
# Setup the list of columns to drop
columns_to_drop = ['Country Code', 'Indicator Code']
columns_to_drop.extend(map(str, range(1960, 2013)))
columns_to_drop.extend(map(str, range(2019, 2023)))
df.drop(columns=columns_to_drop, inplace=True)

# Save the modified DataFrame to a new CSV
df.to_csv('data4 mod.csv', index=False)
print(df.head())
