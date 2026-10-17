import pandas as pd
import numpy as np
#x = pd.read_csv("I:\\GitContent\\Datasets\\Bank_full.csv")
#reading from web to create dataframe
x = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/Bank_full.csv')
df = pd.DataFrame(x)
print(df.columns)
print(x.values)
df[df.age > 80]
df[df.age > 80].education
df[df.age > 80].education.unique()
df.mean()
df.median()
df.mode(axis=1)
df.mode(axis=0)
df[(df.age > 80) & (df.marital=='married')]
df[(df.age > 80) & (df.marital=='married')].sort_values('balance',ascending=False)
df[(df.age.isin(['82','15','17','35']))].head()
df.groupby(['age','y']).size()
df.groupby(['age','y']).size()
#count displays number of non-null/NAN values
df.groupby(['age','y']).count()

#If we want to use different fields for sorting, or DESC instead of ASC
# we want to sort by our calculated field (size), this field needs to become part of 
# the DataFrame. After grouping in Pandas, we get back a different type, called 
# a GroupByObject. 
# So we need to convert it back to a DataFrame. With .reset_index(), we restart 
# row numbering for our data frame.
df.groupby(['marital', 'y']).size().to_frame('size').reset_index().sort_values(['marital', 'size'], ascending=[True, False])

#additionally filter grouped data using a HAVING condition. In Pandas, 
# you can use .filter() and provide a Python function (or a lambda) 
# that will return True if the group should be included into the result.

df[df.marital == 'married'].groupby('y').filter(lambda g: len(g) > 1000) \
.groupby('y').size().sort_values(ascending=False)

#creating new df
df1 = df.groupby(['age','y']).count()

#now getting top N records
df1.nlargest(10, columns='marital')

#getting the next 10 after the top 10
df1.nlargest(20, columns='marital').tail(10)

df[df.y == 'yes'].agg({'age':['mean']})
df.groupby('y').agg({'age':['mean']})

#Use .merge() to join Pandas dataframes. You need to provide which columns to join on
#  (left_on and right_on), and join type: inner (default), 
# left (corresponds to LEFT OUTER in SQL), right (RIGHT OUTER), 
# or outer (FULL OUTER).

df2 = df[(df.age.isin(['82','15','17','35']))]
df2.merge(df[df.y == 'yes'][['age']], left_on='age', right_on='age', how='inner')[['age','marital','y']]

pd.concat([df[df.y == 'no'][['age', 'job','balance']], df[df.y == 'yes'][['job', 'contact']]])

#if inserting (via concat)
df1 = pd.DataFrame({'id': [1, 2], 'name': ['Harry ', 'Ron ']})
df2 = pd.DataFrame({'id': [3], 'name': ['Peter']})
df3 = pd.concat([df1, df2]).reset_index(drop=True)
df3


df.to_csv(...)  # csv file
df.to_hdf(...)  # HDF5 file
df.to_pickle(...)  # serialized object
df.to_sql(...)  # to SQL database
df.to_excel(...)  # to Excel sheet
df.to_json(...)  # to JSON string
df.to_html(...)  # render as HTML table
df.to_feather(...)  # binary feather-format
df.to_latex(...)  # tabular environment table
df.to_stata(...)  # Stata binary data files
df.to_msgpack(...)	# msgpack (serialize) object
df.to_gbq(...)  # to a Google BigQuery table.
df.to_string(...)  # console-friendly tabular output.
df.to_clipboard(...) # clipboard that can be pasted into Excel

