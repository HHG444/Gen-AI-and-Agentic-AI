import pandas as pd
import numpy as np

#Axis indexes with duplicate values
ser11 = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
ser11.index.is_unique

#Data selection with duplicates. 
# Indexing a value with multiple entries returns a Series 
ser11['a']

# Indexing a value with single entries return a scalar value:
ser11['c']

#if DF with duplicate indexes
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
df.loc['b']

#other useful methods
df.sum()
#Passing axis=1 sums over the rows instead:
df.sum(axis=1)

#NA values are excluded unless the entire slice is NA.
df.mean(axis=1, skipna=False)
df.describe()

# x = [12,34,34]
# from statistics import mean
# x = [-1.135797  ,0.088060 ,-0.679053]
# mean(x)

#On non-numeric data, describe produces alternate summary statistics
ser12 = pd.Series(['a', 'a', 'b', 'c'] * 4)
ser12.describe()

ser13 = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = ser13.unique()
uniques
uniques.sort()
uniques

#series of value frequencies
ser11 = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
ser11.value_counts()
##pd.value_counts(ser13.values, sort=False)

#isin :responsible for vectorized set membership
test = ser13.isin(['b', 'c'])
test
ser13[test]