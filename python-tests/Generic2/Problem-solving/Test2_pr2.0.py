#Problem:
'''Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.
You may assume that each input would have exactly one solution, and you may 
not use the same element twice.'''

#Solution1:
class Solution:
    def twoSum(self,nums = [],target: int = 0) -> []:
        newl = []
        for i in nums:
            for j in nums:
                if i+j==target:
                    print("numbers are: " + \
                        str(i) + " and " + str(j))
                    [print(nums.index(i),nums.index(j))]
                    newl.append(nums.index(i))
                    newl.append(nums.index(j))
                    return newl
Solution.twoSum(self="test",nums = [2,7,11,15],target=18)
