import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

employees = pd.cut(ages, bins)
employees

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
employees1 = pd.cut(ages, bins, labels=group_names)
#categorical object i.e array of strings indicating bin name
employees1

#If you pass cut a integer number of bins instead of explicit bin edges, 
# it will compute
#equal-length bins based on the minimum and maximum values in the data.
data = np.random.rand(20)
pd.cut(data, 4, precision=2)

#A closely related function, qcut, bins the data based on sample quantiles.
data = np.random.randn(1000) # Normally distributed
students = pd.qcut(data, 4) # Cut into quartiles
students
pd.value_counts(students)



