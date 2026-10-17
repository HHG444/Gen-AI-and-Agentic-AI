a = [1,2,3,3,3,4,5]
n = len(a)
print(a[2:n])
no_dupes = [x for n, x in enumerate(a) if x not in a[:n]]

print(no_dupes) 

# [[1], [2], [3],[4],[5]]

dupes = [x for n, x in enumerate(a) if x in a[:n]]
print(dupes)
 # [3]]

d = [1,2,3,4,5]
for count,test in enumerate(d,100):
    print(count,test)