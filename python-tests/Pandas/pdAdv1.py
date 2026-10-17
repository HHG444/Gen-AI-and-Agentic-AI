#Data contained in pandas objects can be combined together in a number of built-in ways:
##pandas.merge connects rows in DataFrames based on one or more keys like joins
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})

print(df1)
print(df2)

#many-to-one merge situation
#If not specified, merge uses the overlapping column names as the keys.
pd.merge(df1, df2)
print(pd.merge(df1, df2))

#Specifying
pd.merge(df1, df2, on='key')
print(pd.merge(df1, df2, on='key'))

#if column names are different in each df
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})

print(df3)
print(df4)

pd.merge(df3, df4, left_on='lkey', right_on='rkey')
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

# df5 = pd.read_csv("I:\\GitContent\\Datasets\\Bank_full1_2018.csv")
# df6 = pd.read_csv("I:\\GitContent\\Datasets\\Bank_full1_2019.csv")
# df7 = pd.merge(df5, df6, left_on='y', right_on='y')

#By default merge does an 'inner' join; the keys in the result are the intersection.
#Other possible options are 'left', 'right', and 'outer'.
#Note**The outer join takes the union of the keys, combining the effect of applying 
#both left and right joins.

pd.merge(df1, df2, how='outer')
print(pd.merge(df1, df2, how='outer'))

#Many-to-many merges
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],'data2': range(5)})

print(df1)
print(df2)

pd.merge(df1, df2, on='key', how='left')
print(pd.merge(df1, df2, on='key', how='left'))
#Many-to-many joins form the Cartesian product of the rows

pd.merge(df1, df2, how='inner')
print(pd.merge(df1, df2, how='inner'))

#To merge with multiple keys, pass a list of column names:
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],'key2': ['one', 'two', 'one'],'lval': [1, 2, 3]})
print(left)

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],'key2': ['one', 'one', 'one', 'two'],'rval': [4, 5, 6, 7]})
print(right)

pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
#above multiple keys can be thgt as forming an array of tuples to be used
#as a single join key

#treatment of overlapping column names.
#using suffixes option for specifying strings to append to overlapping
#names in the left and right DataFrame objects
pd.merge(left, right, on='key1')
print(pd.merge(left, right, on='key1'))

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))

#Merging on indexes
#if merge key or keys in a DataFrame will be found in its index. 
# In this case, you can pass left_index=True or right_index=True (or both) 
# to indicate that the index should be used as the merge key

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

pd.merge(left1, right1, left_on='key', right_index=True)
print(pd.merge(left1, right1, left_on='key', right_index=True))

#forming union using outer join
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))


#if hierarchial indexed dat
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'key2': [2000, 2001, 2002, 2001, 2002],
'data': np.arange(5.)})

print(lefth)

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
[2001, 2000, 2000, 2000, 2001, 2002]],
columns=['event1', 'event2'])
print(righth)


#we have to indicate multiple columns to merge on as a list
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))

pd.merge(lefth, righth, left_on=['key1', 'key2'],right_index=True, how='outer')
print(pd.merge(lefth, righth, left_on=['key1', 'key2'],right_index=True, how='outer'))

#Using the indexes of both sides of the merge
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))

#DataFrame has join instance for merging by index. It can also be
#used to combine together many DataFrame objects having the same or similar indexes
#but non-overlapping columns. 
# In the prior example, we could have written:
left2.join(right2, how='outer')
print(left2.join(right2, how='outer'))

#joining the index with a column
left1.join(right1, on='key')
print(left1.join(right1, on='key'))

#for simple index-on-index merges, you can pass a list of DataFrames to join
Test = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])

left2.join([right2, Test])
print(left2.join([right2, Test]))

left2.join([right2, Test], how='outer')
print(left2.join([right2, Test], how='outer'))


##pandas.concat glues or stacks together objects along an axis.
##combine_first instance method enables slicing together overlapping data to fill
#in missing values in one object with values from another.

