import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv', skiprows=19)
print(f"{df.head(5)}\n")

corrtemp = df["month"].corr(df["meant"])
print(f"Temperature correlation is: {corrtemp}\n")

# Extract columns without creating a copy
cleandf = df.loc[:, ["month", "wdsp"]] 
# Replace spaces with NaN in 'wdsp' column
cleandf['wdsp'] = cleandf['wdsp'].replace(' ', np.nan)
# Drop rows with NaN values in 'wdsp' column 
cleandf.dropna(subset=['wdsp'], inplace=True)
# Convert 'wdsp' column to float
cleandf['wdsp'] = cleandf['wdsp'].astype(float)
# Calculate correlation between 'month' and 'wdsp' columns
corrwind = cleandf["month"].corr(cleandf["wdsp"])
print (f"wWnd correlation is: {corrwind}")

sns.set_style('whitegrid')
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf)
plt.show()