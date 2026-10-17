from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

#Boxplot of Month-wise (Seasonal) and Year-wise (trend) Distribution
ser = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/a10.csv', parse_dates=['date'], index_col='date')
ser.head()
print(ser.head())
ser.reset_index(inplace=True)

# Prepare data
ser['year'] = [d.year for d in ser.date]
ser['month'] = [d.strftime('%b') for d in ser.date]
years = ser['year'].unique()

# Draw Plot
fig, axes = plt.subplots(1, 2, figsize=(14,7), dpi= 80)
sns.boxplot(x='year', y='value', data=ser, ax=axes[0])
sns.boxplot(x='month', y='value', data=ser.loc[~ser.year.isin([1991, 2008]), :])

# Set Title
axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18); 
axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)
plt.show()

#The boxplots make the year-wise and month-wise distributions evident. 
# Also, in a month-wise boxplot, the months of December and January clearly has 
# higher drug sales, which can be attributed to the holiday discounts season.


