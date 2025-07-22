from unittest.mock import inplace

import pandas as pd

# Load supermarket sales data
df = pd.read_excel('supermarket_sales.xlsx')
df = df[['Gender', 'Product Line', 'Total']]

# Create pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product Line', values='Total', aggfunc='sum').round(0)
#print(pivot_table)

# Export to Excel
pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report', startrow=4)

# ✅ Load football data (now works after certificate fix)
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')

df_premier21.rename(columns={
    'FTHG':'home_goals',
    'FTAG':'away_goals',
},inplace=True)
print(df_premier21.head())
