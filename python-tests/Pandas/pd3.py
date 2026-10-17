#Pandas: Index Objects
#pandas’s Index objects are responsible for holding the axis labels and other metadata
#Any array/sequence of labels used while series/df are converted to an index.
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
item = pd.Series(range(3),index = ['a','b','c'])
print(item)
index = item.index
print(index)

index[1:]
print(index[1:])

type(item)
type(index)
#index[0]
index[0]='try this to check mutability'

index

# indexTest = pd.Index(np.arange(3))
# print(indexTest)
# print('*' * 50)
# item2 = pd.Series([1,2,3],index=indexTest)

# item2

# item2.index
# item2.index is indexTest
# print(item2.index is indexTest)

#Apart from being array-like, an Index also functions as a fixed-size set:
pop = {'norway': {2001: 2.4, 2002: 2.9},
'denmark': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)

'norway' in frame3.columns
print('norway' in frame3.columns)

2003 in frame3.index
print(2003 in frame3.index)