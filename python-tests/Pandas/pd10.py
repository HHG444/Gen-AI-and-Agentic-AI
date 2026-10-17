import pandas as pd
import numpy as np

#Hierarchial Indexing
#Enables you to have multiple (two or more) index levels on an axis. 
# It provides a way for you to work with higher dimensional data in a lower 
# dimensional form.
data = pd.Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data
#we see a view of a Series with a MultiIndex as its index

data.index

#now we can do a partial indexing & select subsets of the data
data['b']
data['b':'c']
data.loc[['b', 'd']]

#selection from inner level
data[:, 2]

#Hierarchical indexing plays a critical role in reshaping data and group-based operations.
#like forming a pivot table. 
# For example, this data could be rearranged into a DataFrame using its unstack method:
data.unstack()
data.unstack().stack()

#With a DataFrame, either axis can have a hierarchical index
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['germany', 'france', 'sweden'],
['Green', 'Red', 'Orange']])
frame

#The hierarchical levels can have names
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'zone']
frame

#With partial column indexing you can similarly select groups of columns
frame['germany']

#Reordering and sorting levels
#to rearrange the order of the levels on an axis or sort the data
#by the values in one specific level.


#The swaplevel takes two level numbers or names and
#returns a new object with the levels interchanged
frame.swaplevel('key1', 'key2')

#Many descriptive and summary statistics on DataFrame and Series have a level option
#in which you can specify the level you want to sum by on a particular axis.
frame.sum(level='key2')

frame.sum(level='zone', axis=1)


#Using a DataFrame’s Columns for indexing
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
'd': [0, 1, 2, 0, 1, 2, 3]})
frame

#set_index function will create a new DataFrame using one or more of its
#columns as the index
frame2 = frame.set_index(['c', 'd'])
frame2

#By default the columns are removed from the DataFrame,but we can leave them
frame.set_index(['c', 'd'], drop=False)

#moving hierarchial index into columns
#reset_index, on the other hand, does the opposite of set_index
frame2.reset_index()






