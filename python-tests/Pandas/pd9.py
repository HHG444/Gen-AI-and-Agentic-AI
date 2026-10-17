import pandas as pd
import numpy as np

#Handling Missing Data
#Note**All of the descriptive statistics on pandas objects exclude missing data.
string_data = pd.Series(['apple', 'orange', np.nan, 'avocado','grapes'])
string_data
string_data.isnull()

#built-in Python None value is also treated as NA in object arrays
string_data[0] = None
string_data
string_data.isnull()

#dropna Filter axis labels based on whether values for each label have missing data, 
# with varying thresholds for how much missing data to tolerate.
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()
data.notnull()
#by boolean indexing method
data[data.notnull()]

#in df, we may want to drop rows/columns which are all NAs or those just containing NAs
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
[NA, NA, NA], [NA, 6.5, 3.]])

cleaned_data = data.dropna()
cleaned_data

#To only drop rows that are all NA
data.dropna(how='all')

#Dropping columns by passing axis=1
data[4] = NA
data
data.dropna(axis=1, how='all')

#To keep only rows containing a certain number of observations
#using thresh
df = pd.DataFrame(np.random.randn(7, 3))
df
df.loc[:4, 1] = NA
df.loc[:2, 2] = NA
df
df1=df.dropna(thresh=2)
df1

#Filling Missing Data
df
df.fillna(0)

#Calling fillna with a dict you can use a different fill value for each column
df
df.fillna({1: 0.5, 2: -1})

#modify the existing object in place instead of returning a new object
_ = df.fillna(0, inplace=True) #always returns a reference to the filled object
df

#using ffill
df = pd.DataFrame(np.random.randn(6, 3))
df.loc[2:, 1] = NA
df.loc[4:, 2] = NA
df
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)

#using fillna and passing mean/median 
data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())






