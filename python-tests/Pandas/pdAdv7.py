import pandas as pd
import numpy as np
import datetime
raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'red', 'yellow', "green"],
'grade': [88, 92, 95, 70],
'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
print(df.head)

#efficient way to extract year from string format date
df['year'] = pd.DatetimeIndex(df['birth_date']).year
print(df.head())

#create a new column with month of date field 'birth_date'
df['month'] = pd.DatetimeIndex(df['birth_date']).month
print(df.head())

#if the date format comes in datetime, we can also extract the day/month/year 
# using the to_period function #where 'D', 'M', 'Y' are inputs
df['month_year'] = pd.to_datetime(df['birth_date']).dt.to_period('M')
df.head()

