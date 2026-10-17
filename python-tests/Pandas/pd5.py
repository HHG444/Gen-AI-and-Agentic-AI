import pandas as pd
import numpy as np
#series indexing 
ser7 = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(ser7)
print(ser7['a'])
print(ser7[1])
print(ser7[1] == ser7['b'])
print(ser7[2:4])
print(ser7[[1,3]])
print(ser7[ser7>2])

#Slicing with labels behaves differently than normal Python slicing in that the endpoint
#is inclusive
print(ser7['b':'c'])

#setting values
ser7['b':'c'] = 5
print(ser7)

#indexing into a DataFrame
data1 = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['paris', 'belgium', 'vienna', 'basel'],
columns=['one', 'two', 'three', 'four'])
print(data1)

print(data1['two'])
print(data1[['three','one']])
print(data1[:2])
print(data1[data1['three'] > 5])

#indexing with a boolean DataFrame
print(data1 < 5)

data1[data1 < 5] = 0
print(data1)

#For DataFrame label-indexing on the rows
print(data1)
print(data1.loc['belgium',['two','three']])
print(data1.loc[['belgium', 'paris'], ['two','three']])
print(data1.loc[:'belgium','two'])

#Arthimetic and Data Alignment
#arithmetic operation between objects with different indexes. When adding together objects, 
# if any index pairs are not the same, the respective index in the result will be the union of the index pairs.

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1+s2)

#In the case of DataFrame, alignment is performed on both the rows and the columns:
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df3 = pd.DataFrame([np.arange(3)],columns=['a','b','c'],index=['values'])
df3
#Adding returns a DataFrame whose index and columns are the unions of the ones in each DataFrame:
print(df1+df2)

#Arithmetic methods with fill values
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1+df2)

#using add method
print(df1.add(df2, fill_value=0))

#when reindexing a Series or DataFrame, you can also specify a different fill value
print(df1.reindex(columns=df2.columns, fill_value=0))