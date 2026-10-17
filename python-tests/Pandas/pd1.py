#Working with Series 
#from pandas import Series, DataFrame
import pandas as pd

import numpy as np

#Series
ser = pd.Series([4, 7, -5, 3])
print(ser)
print('*'*100)


#we can see index on the left and the values on the right. 
# Since we did not specify an index for the data, a default
#consisting of the integers 0 through N - 1 (where N is the length of the data) is created.
#You can get the array representation and index object of the Series via its values
#and index attributes, respectively.
print(ser.values)
print(ser.index)
print('*'*100)

#to create a Series with an index identifying each data point
ser2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
#ser2.index
print(ser2.index)
print('*' * 100)

#manipulating and accessing values of series
print(ser2['a'])
ser2['d'] = 6
print(ser2[['c', 'a', 'd']])
print('*' * 100)
#NumPy array operations, such as filtering with a boolean array, 
# scalar multiplication,
#or applying math functions, preserve the index-value link
print(ser2)
print(ser2[ser2 > 0])
print(ser2 * 2)
print(np.exp(ser2))
print('*'*100)
#Note the unchanged index values

#Series is a fixed-length, ordered dict, as it is a mapping of index values 
# to data values.
print('b' in ser2)
print('e' in ser2)
print('*' * 100)

#If you have data contained in a Python dict, you can create a Series from it 
# by passing the dict:
sdata = {'france': 35000, 'germany': 71000, 'greece': 16000, 'norway': 5000}
ser3 = pd.Series(sdata)
print(ser3)
print(ser3.index)
print(ser3.values)
print('*'*100)

#When only passing a dict, the index in the resulting Series will have the 
# dict’s keys in sorted order
country = sorted(['greece', 'france', 'germany', 'norway'])
country
ser4 = pd.Series(sdata, index=country)
print(ser4)
print('*'*100)

#The isnull and notnull functions in pandas should be used to detect missing data
pd.isnull(ser4)
pd.notnull(ser4)
print('*'*100)

#Series also has these as instance methods
print(ser4.isnull())
print('*'*100)

#A critical Series feature for many applications is that it automatically 
# aligns differently indexed
#data in arithmetic operations:
print(ser3)
print(ser4)
print(ser3 + ser4)
print('*'*100)

#Both the Series object itself and its index have a name attribute, which integrates with
#other key areas of pandas functionality:
ser4.name = 'population'
ser4.index.name = 'country'
print(ser4)
print('*'*100)

#A Series’s index can be altered in place by assignment
ser.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

print(ser)

print('*'*10)








