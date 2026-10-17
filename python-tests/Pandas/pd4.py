
#Reindexing
#to create a new object with the data confirmed to a new index.
import pandas as pd
import numpy as np
ser = pd.Series([1,2,3,4], index=['d','b','c','a'])
print(ser)

#calling reindex to rearrange data as per new index
ser1 = ser.reindex(['a','b','c','d'])
print(ser1)

print(ser)

ser3 = ser1.reindex(['a','b','c','d','e'])
#ser3 = ser1.reindex(['a','test1','b','test2','c','test3','d','test4','e'])
print(ser3)

ser3 = ser1.reindex(['a','b','c','d','e'],fill_value=0)
print(ser3)

#using ffill to take care of missing values (interpolation/filling values)
ser4 = pd.Series(['cricket','football','basketball'],index=[0,2,4])
ser4
print(ser4)

ser4.reindex(range(6),method='ffill')
print(ser4.reindex(range(6),method='ffill'))

ser5 = pd.Series(['cricket','football','basketball'],index=[0,2,4])
ser5
print(ser5)

ser5.reindex(range(6),method='bfill')
print(ser5.reindex(range(6),method='bfill'))

#With DF , reindex can alter the row-index, columns or both
frame = pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],
columns=['ger','aus','fra'])
print(frame)

frame2 = frame.reindex(['a','b','c','d'])
print(frame2)

#columns can be reindexed using the columns keyword
country = ['ger','norway','fra']
frame.reindex(columns = country)
print(frame.reindex(columns = country))

#frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',columns=country)
frame.loc[['a', 'b', 'c', 'd'], country]
print(frame.loc[['a', 'b', 'c', 'd'], country])

#dropping entries from an axis
#Dropping one or more entries from an axis is easy if you have an index array or list
#without those entries.
ser6 = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
ser6
new_ser = ser6.drop('c')
new_ser
print(new_ser)

print(ser6.drop(['a','c']))
ser6

#With DataFrame, index values can be deleted from either axis:
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['paris', 'belgium', 'vienna', 'basel'],
columns=['one', 'two', 'three', 'four'])

print(data)
print(data.drop(['paris','belgium']))

print(data)
print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis=1))



