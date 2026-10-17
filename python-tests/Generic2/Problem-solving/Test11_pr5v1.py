#print('get length of list')
#m = len(l)
#print(m)
#print('index starts at',l.index(l[0]))
#print('index ends at',l.index(l[len(l)-1]))

#print('we want to find duplicate numbers in the list which has ',m-1,'elements')
print('option1')
l = [1,2,3,4,4,5,6,6,7,8,13,14,14,15,16,88]
x = set()
y = []
for n in l:
    if n not in x:
        y.append(n)
        x.add(n)
print(y)
print('-' * 50)

#
print('option 2')
no_dupes = [x for n, 
x in enumerate(l) 
if x not in l[:n]]
print(no_dupes)

