#1
def mysum(n):
    return n * 1000

mysum(20)

#2
mylist = [23,34,45,56,67]
newlist = []

for i in mylist:
    newlist.append(mysum(i))

newlist

#3
mylist2 = [23,34,45,56,67]
preflist = list(map(lambda n: n*100,mylist2))
preflist

#4
sellist = list(filter(lambda i: i%2==0,mylist2))
sellist

#5
preflist = list(map(lambda n: mysum(n),mylist2))
preflist




