import numpy as np
#first numpy array
first_numpy_array = np.array([1,3,5,7])
print(first_numpy_array)

#array with zeroes
array_with_zeroes = np.zeros((3,3))

print(array_with_zeroes)

#array with ones
array_with_ones = np.ones((3,3))
print(array_with_ones)


array_with_ones.shape
array_with_ones.size
array_with_ones.dtype
array_with_ones.ndim

#array with empty (puts in random values)
array_with_empty = np.empty((2,3))
print(array_with_empty)

#array with arange method to create arrays of certain data length
np_arange = np.arange(12)
print(np_arange)

#reshaping 1-dimensional to 2-dimensional or say 3 rows and 4 columns (using reshape method)
np_arange.reshape(3,4)
print(np_arange.reshape(4,3))
print(np_arange.reshape(3,4))
print(np_arange.reshape(6,2))
print(np_arange.reshape(2,6))
print(np_arange.reshape(1,12))
print(np_arange.reshape(12,1))

#linspace for linearly (equal) spaced data elements
np_linspace = np.linspace(1,6,5) #first ele,last ele & total no of equidistant elements
print(np_linspace)

np_linspace = np.linspace(1,10,4)
np_linspace

#one dimensional array
oneD_array = np.arange(15)
print(oneD_array)

#2 dimensional array
twoD_array = oneD_array.reshape(3,5)
print(twoD_array)

#3 dimensional array
threeD_array = np.arange(27).reshape(3,3,3)
print(threeD_array)









