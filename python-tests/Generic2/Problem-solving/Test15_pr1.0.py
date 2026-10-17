count = 0
for iterv in [3,45,56,34,23,43]:
    count = count + 1
print('count',count)

total = 0
for iterv in [3,45,56,34,23,43]:
    total = total + iterv
print(total)

largest = None
print ('Before:',largest)
for iterv in [2,3,45,54,45,53,100,1]:
    if largest == None or iterv > largest:
        largest = iterv
    print('Loop:',iterv,largest)
print('largest number is: ',largest)
