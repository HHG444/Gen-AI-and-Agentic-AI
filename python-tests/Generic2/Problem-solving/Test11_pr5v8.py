#Third party library
#from iteration_utilities import duplicates
#list(duplicates([1,1,2,1,2,3,4,2]))

import pandas as pd
a = [1, 2, 1, 3, 3, 3, 0]
print(pd.Series(a)[pd.Series(a).duplicated()].values)

