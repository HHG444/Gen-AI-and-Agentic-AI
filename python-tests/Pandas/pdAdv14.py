import pandas as pd
import datetime
import numpy as np
#create some sample data that we can group by time

# Create a datetime variable for today
base = datetime.datetime.today()
base
# Create a list variable that creates 365 days of rows of datetime values
date_list = [base - datetime.timedelta(days=x) for x in range(0, 365)]
print(date_list[0:5])

# Create a list variable of 365 numeric values
score_list = list(np.random.randint(low=1, high=1000, size=365))
score_list
# Create an empty dataframe
df = pd.DataFrame()

# Create a column from the datetime variable
df['datetime'] = date_list
# Convert that column into a datetime datatype
df['datetime'] = pd.to_datetime(df['datetime'])
# Set the datetime column as the index
df.index = df['datetime'] 
# Create a column from the numeric score variable
df['score'] = score_list

print(df.head())

#In pandas, the most common way to group by time is to use the .resample() function. 
# In v0.18.0 this function is two-stage. This means that 
# ‘df.resample(’M’)’ creates an object to which we can apply other
#  functions (‘mean’, ‘count’, ‘sum’, etc.)

# Group the data by month, and take the mean for each group (i.e. each month)
res1 = df.resample('M').mean()
print(res1)

# Group the data by month, and take the sum for each group (i.e. each month)
res2 = df.resample('M').sum()
print(res2)

