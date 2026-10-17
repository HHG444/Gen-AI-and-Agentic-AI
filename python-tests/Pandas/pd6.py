#operations between dataframe and series
import pandas as pd
import numpy as np
arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
arr-arr[0] #example of broadcasting
print(arr)

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['germany', 'austria', 'russia', 'sweden'])

print(frame)
series = frame.loc['germany']
print(series)
series1 = frame.loc[['germany']]
series1

#arithmetic between DataFrame and Series matches the index of the Series
#on the DataFrame's columns, broadcasting down the rows
print(frame - series)

#If an index value is not found in either the DataFrame’s columns or the Series’s index,
#the objects will be reindexed to form the union
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame+series2)

#to broadcast over the columns, matching on the rows, use one of the arithmetic methods.
series3 = frame['d']

print(frame)

print(series)

print(frame.sub(series3, axis=0))