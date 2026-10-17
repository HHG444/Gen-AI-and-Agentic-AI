#1
import math
print(math.sqrt(4))

x = ['cool','winter','summer']
z = list(map(lambda n: n.upper(),x))
for i in z:
    print(i)
type(z)
print(z)

#2
def testf():
    yield 10
    yield 20
    yield 30
    yield 40

for i in testf():
    print(i)

#3
def testnum():
    i = 1
    while True:
        yield i*i
        i += 1

for n in testnum():
    if n > 20:
        break
    print(n)

#More examples to be added

