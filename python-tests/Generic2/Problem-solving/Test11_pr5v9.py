myList  = [2,4,6, 8, 4, 6,6,12]
newList = set()
for i in myList:
    if myList.count(i) >= 2:
        newList.add(i)
print(list(newList))
