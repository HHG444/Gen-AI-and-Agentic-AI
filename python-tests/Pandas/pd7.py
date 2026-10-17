import numpy as np
import pandas as pd

#Applying functions/mapping
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
index=['germany', 'austria', 'russia', 'sweden'])
frame
type(frame)
np.abs(frame)

f = lambda x: x.max() - x.min()
print(frame.apply(f))

print(frame.apply(f, axis=1))

def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

#Element-wise Python functions can be used, too. To compute a
#formatted string from each floating point value in frame. use applymap
format = lambda x: '%.2f' % x
print(frame.applymap(format))
print(frame.applymap(lambda n: '%.2f' % n))

#map method in series for element-wise function
print(frame['e'].map(format))

#Sorting & Ranking
#To sort lexicographically by row or column index, use the sort_index method
ser8 = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(ser8)
print(ser8.sort_index())

#With a DataFrame, you can sort by index on either axis
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])

print(frame.sort_index())
print(frame.sort_index(axis=0))
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))

#sorting dataframe by values
import pandas as pd
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a', 'b']))

#Ranking
#Ranking is closely related to sorting, assigning ranks from 1 to all valid data points
# in an array. The rank methods for Series and DataFrame breaks ties by assigning
#each group the mean rank

#Pandas Series.rank() function compute numerical data ranks (1 through n) along axis. 
#Equal values are assigned a rank that is the average of the ranks of those values.

# Syntax: Series.rank(axis=0, method=’average’, numeric_only=None, na_option=’keep’, ascending=True, pct=False)

# Parameter :
# axis : index to direct ranking
# method : {‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}
# numeric_only : Include only float, int, boolean data. Valid only for DataFrame or Panel objects
# na_option : {‘keep’, ‘top’, ‘bottom’}
# ascending : False for ranks by high (1) to low (N)
# pct : Computes percentage rank of data

# Returns : ranks : same type as caller

ser10 = pd.Series([7,-5,7,4,2,0,4])
print(ser10)
print(ser10.rank())
print(ser10.rank(ascending = False))
#Ranks can also be assigned according to the order they’re observed in the data
print(ser10.rank(method='first'))
print(ser10.rank(ascending=False, method='max'))

#DataFrame can compute ranks over the rows or the columns:
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis=1))


