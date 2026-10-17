#####
#1 Testing 
lst = ['we need more storage','we need more space']
l = []
for i in lst:   
    for n in i.split():
        l.append(n)
k = ["storage","space"]
for i in l:     
    for n in k:
        if i == n:
            print(i,l.count(i)) 

#2 Testing 
lst = ['we need more storage',
'we need more space',
'we need more storage',
'we need more space',
'we need more space',
'storage is important',
'more storage','zmemory']
k = ["storage","space","zmemory"]
def test(lst=[],k =[]):
    l = []
    m = set()
    for i in lst:   
        for n in i.split():
            l.append(n)
    for j in k:
        for i in l:
            if j==i:
                m.add((l.count(i),j))
                u = sorted(list(m),reverse = True)
    return u[0:2]

test(lst=lst,k=k)
            
    



