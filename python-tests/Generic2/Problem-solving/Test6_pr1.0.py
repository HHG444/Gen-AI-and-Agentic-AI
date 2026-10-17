mystring = "hadoop is a technology used for bigdata"
newcont = mystring.split(" ")
for x in newcont:
    if x == "hadoop":
        i1 = newcont.index(x)
        print(i1)
        print('*'*10)
newcont.remove(x)
newcont[i1] = "NoSQL"
for i in newcont:
    print(i)

    
       


    