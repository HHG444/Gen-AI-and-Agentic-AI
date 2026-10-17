args = [12,12,13,14,15,16,17]
#def newf(*args):
#   print('option1')
x = set()
y = []
for n in args:
    if n not in x:
        y.append(n)
        x.add(n)
for i in y:
    print(i)


