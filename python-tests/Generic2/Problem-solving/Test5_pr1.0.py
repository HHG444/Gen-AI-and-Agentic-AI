
list2 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
          ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]

for i in list2:
    print(i)

list3 = []

for i in list2:
    list3.extend(i)
list3

def testf(x = []):
    my = set()
    for i in x:
        if type(i) == str:
            my.add((i,x.count(i)))
    return list(my)

list3
testf(list3)

###########################
#using list comprehension
list4 = [[l,list3.count(l)] for l in set(list3) if type(l) == str]
for i in list4:
    print(i)

#############################

lis2 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
          ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]

def newd(l=[]):
    lis = []
    for i in lis2:
        lis.extend(i)
    lis3 = [[lis.count(l),l] for l in set(lis) if type(l)==str]
    return sorted(lis3,reverse = True)

newd(lis2)


    
