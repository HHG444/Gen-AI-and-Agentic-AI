import pandas as pd
import numpy as np

#DataFrame
#A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, 
#each of which can be a different value type (numeric,string, boolean, etc.). The DataFrame has both a row and 
#column index; it can be thought of as a dict of Series (one for all sharing the same index). 

#create a dataframe from a dict of equal-length lists or NumPy arrays
data = {'eucountry': ['france', 'germany', 'austria', 'sweden', 'Norway'],
'year': [2000, 2001, 2002, 2001, 2002],
'popul': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)


#index assigned automatically as with Series, and the columns are placed in sorted order
#print(frame)

#if we specify a sequence of columns, the DataFrame’s columns will be exactly what we pass
print(pd.DataFrame(data, columns=['year', 'eucountry', 'popul']))
framenew = pd.DataFrame(data, columns=['year', 'eucountry', 'popul'])
print(framenew)

#As with Series, if you pass a column that isn’t contained in data, it will appear with NA values in the result
frame2 = pd.DataFrame(data, columns=['year', 'eucountry', 'popul', 'debt'],
index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2.columns)

#A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:
print(frame2['eucountry'])
print(frame2.year)


#Rows can also be retrieved by position or name or such as the ix indexing field
print(frame2.ix['three'])

#FutureWarning: 
#.ix is deprecated. Please use
#.loc for label based indexing or
#.iloc for positional indexing

print(frame2.loc['three'])
print(frame2.loc[['three','one']])
print(frame2.iloc[3])

#Columns can be modified by assignment. For example, the empty 'debt' column could be assigned a scalar 
#value or an array of values
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] == 100
frame2['debt'] != 100
frame2


frame2['debt'] = np.arange(5.)
print(frame2)

frame2['debt'] = range(5)
frame2

#When assigning lists or arrays to a column, the value’s length must match the length
#of the DataFrame. If you assign a Series, it will be instead conformed exactly to the
#DataFrame’s index, inserting missing values in any holes:
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

#Assigning a column that doesn’t exist will create a new column. 
frame2['eastern'] = frame2.eucountry == 'france'
print(frame2)

frame2['abvthold'] = frame2.popul > 1.6
frame2

#The del keyword will delete columns as with a dict:
del frame2['eastern']
del frame2['abvthold']
print(frame2.columns)

frame2

#The column returned when indexing a DataFrame is a view on the underlying
#data, not a copy. Thus, any in-place modifications to the Series
#will be reflected in the DataFrame. The column can be explicitly copied
#using the Series’s copy method.


#Another common form of data is a nested dict of dicts format:
pop = {'norway': {2001: 2.4, 2002: 2.9},'denmark': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
pop
#If passed to DataFrame, it will interpret the outer dict keys as the columns and the inner
#keys as the row indices:
frame3 = pd.DataFrame(pop)
print(frame3)

#you can always transpose the result
print(frame3.T)


#The keys in the inner dicts are unioned and sorted to form the index in the result. This
#isn’t true if an explicit index is specified:
pd.DataFrame(pop, index=[2001, 2002, 2003])
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

#Dicts of Series are treated much in the same way:
pdata = {'norway': frame3['norway'][:-1],
'denmark': frame3['denmark'][:2]}
pd.DataFrame(pdata)

#If a DataFrame’s index and columns have their name attributes set, these will also be
#displayed:
print(frame3)
frame3.index.name = 'year'; 
frame3.columns.name = 'eucountry'

print(frame3)

#Like Series, the values attribute returns the data contained in the DataFrame as a 2D #ndarray:
print(frame3.values)

#If the DataFrame’s columns are different dtypes, the dtype of the values array will be
#chosen to accomodate all of the columns:
print(frame2.values)







