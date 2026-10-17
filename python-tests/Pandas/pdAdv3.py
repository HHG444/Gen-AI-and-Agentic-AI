#Reshaping with Hierarchical Indexing
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
index=pd.Index(['india', 'europe'], name='ctry'),
columns=pd.Index(['one', 'two', 'three'], name='number'))
data
print(data)

#stack method on this data pivots the columns into the rows
result = data.stack()
result
print(result)

#rearrange the data back into a DataFrame
result.unstack()
print(result.unstack())
result.unstack(0)
print(result.unstack(0))

result.unstack('ctry')
print(result.unstack('ctry'))

#if missing data introduced by unstacking
result.unstack().stack(dropna=False)
print(result.unstack().stack(dropna=False))



