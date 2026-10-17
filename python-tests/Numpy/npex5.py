import numpy as np
#broadcasting 
array_a = np.array([2,34,5,8])
array_b = np.array([.3,.3,.3,.3])

result = array_a * array_b
print(result)

#variable with a scalar value
scalar_c = 0.3

#multiple array with scalar value
result2 = array_a * scalar_c
print(result2)

nums1 = np.array([1,2,4,3])
nums2 = np.array([4])
nums1.ndim
nums2.ndim
nums1.shape
nums2.shape
nums1*nums2
