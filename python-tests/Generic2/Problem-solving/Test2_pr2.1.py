#working with list
mylist = [4,3,2,9,10,44,1]
mylist
mylist.sort()
mylist
midvalue = mylist[int(len(mylist)/2)]
midvalue

#Attempt-1
# # #Finding two numbers whose sum is x from a list
mylist = [1,2,3,4,9,7,11,8,13,19,20,18]
target=38
class solution:
    def midfind(self,list = [],target=0):
        list.sort()
        lele = len(list)
        mid = int(lele/2)
        t = list[mid]
        if target>t:
            listN = list[mid:lele]
            for i in listN:
                for j in listN:
                    if i+j==target:
                        return [list.index(i),list.index(j)]
                        
        else:
            listN = list[0:mid]
            for i in listN:
                for j in listN:
                    if i+j==target:
                        return [list.index(i),list.index(j)]
                        
solution.midfind(self="test",list=mylist,target=3)
#solution.midfind(self="test1",list = mylist,target=32)

#Attempt-2
from typing import List
class solution:
    def twoSum(self,nums: List[int],target: int) -> List[int]:
        nums.sort()
        lele = len(nums)
        mid = int(lele/2)
        t = nums[mid]
        if target>t:
            numsx = nums[mid:lele]
            newl = []
            for i in numsx:
                for j in numsx:
                    if i+j==target:
                        newl.append(nums.index(i))
                        newl.append(nums.index(j))
                        return newl
                        
        else:
            numsx = nums[0:mid]
            newl = []
            for i in numsx:
                for j in numsx:
                    if i+j==target:
                        newl.append(nums.index(i))
                        newl.append(nums.index(j))
                        return newl

mylist = [1,2,3,4,9,7,11,8,13,19,20,18]
solution.twoSum(self="test",nums = mylist,target=7)