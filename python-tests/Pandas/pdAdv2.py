import numpy as np
import pandas as pd

#Concat along an axis (concate,bind,stack)
arr = np.arange(12).reshape((3, 4))
print(arr)
np.concatenate([arr, arr], axis=1)
print(np.concatenate([arr, arr], axis=1))

np.concatenate([arr, arr], axis=0)
print(np.concatenate([arr, arr], axis=0))

#series with no index overlap
#By default concat works along axis=0, producing another Series.

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
pd.concat([s1, s2, s3])
print(pd.concat([s1, s2, s3]))

#If you pass axis=1, the result will instead be a DataFrame (axis=1 for columns):
pd.concat([s1, s2, s3], axis=1)
print(pd.concat([s1, s2, s3], axis=1))
#shows sorted union (the 'outer' join) of the indexes.

#intersect them by using join='inner'
s4 = pd.concat([s1 * 5, s3])
s4

pd.concat([s1, s4], axis=1)
print(pd.concat([s1, s4], axis=1))

s1
s4
pd.concat([s1, s4], axis=1, join='inner')
print(pd.concat([s1, s4], axis=1, join='inner'))

n = pd.concat([s1, s4], axis=1)
n.reindex(['a', 'c', 'b', 'e'])

#creating a hierarchical index on the concatenation axis
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result
print(result)

#When combining Series along axis=1, the keys become the DataFrame column headers:
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))

#for Dataframes
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],columns=['three', 'four'])

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
pd.concat([df1, df2], axis=0, keys=['level1', 'level2'])

#Using dict of objects instead of a list, the dict’s keys will be used for the keys
pd.concat({'level1': df1, 'level2': df2}, axis=1)
print(pd.concat({'level1': df1, 'level2': df2}, axis=1))

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],names=['upper', 'lower'])
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],names=['upper', 'lower']))

#ignoring indexes that are not meaningful
df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
pd.concat([df1, df2], ignore_index=True)
print(pd.concat([df1, df2], ignore_index=True))

#combining when overlap i.e. when two datasets have indexes in full overlapping
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
print(a)
print(b)

#option1
np.where(pd.isnull(a), b, a)
print(np.where(pd.isnull(a), b, a))

#option 2

b[:-2].combine_first(a[2:])
print(b[:-2].combine_first(a[2:]))

#combine first in dataframe
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],'b': [np.nan, 2., np.nan, 6.],'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],'b': [np.nan, 3., 4., 6., 8.]})
df1.combine_first(df2)
print(df1.combine_first(df2))