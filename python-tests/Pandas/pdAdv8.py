#Vectorized operations in series
import numpy as np
import pandas as pd
first_vector_series = pd.Series([1,2,3,4],index=['a','b','c','d'])
second_vector_series = pd.Series([10,20,30,40],index=['a','b','c','d'])
print(first_vector_series+second_vector_series)

second_vector_series = pd.Series([10,20,30,40],index=['a','d','b','c'])
print(first_vector_series+second_vector_series)
