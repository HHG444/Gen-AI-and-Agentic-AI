#1 Working with tuples (espescially using when we needunmodifiable list)
#note** tuples are immutable

numbers = (1,2,3,5,6)
print(numbers)
print(numbers[0])

for i in numbers:
    print(i)

numbers.count(1)

tup = 4, 5, 6
type(tup)
print(tup)

#creating a tuple of tuples
nested_tup = (4, 5, 6), (7, 8)
print(nested_tup)

for i in nested_tup:
    print(i[0])
len(nested_tup)

#converting sequence/iterator to tuple
x = tuple([4, 0, 2])
print(x)
type(x)

a = [1,2,3,4,5]
type(a)

t_a = tuple(a)
print(t_a)
type(t_a)

t_l = list(t_a)
print(t_l)
type(t_l)

tup = tuple('hello world')
print(tup)

#slicing in tuples
tup[0:2]
tup[1:]
tup[:1]
tup[:-1]
tup[-5:-1]

tup = tuple(['foo', [1, 2], True])
tup(2) = False
print(tup)

#'tuple' object does not support item assignment

tup[1].append(3)
tup

#concatenating tuples
xccat = (4, None, 'hello') + (6, 0) + ('world',)
xccat

#xccat1 = (4, None, 'hello') + (['hello':'world']) + ('world',) #throws error

#concatenating via multiplication
xccat2 = ('fool', 'barbie') * 4
xccat2

xcclst = ['hello','hi'] * 4
xcclst

#unpacking tuples
tup = (1,2,3)
a,b,c = tup
a
b
c

x,y,z = 100,200,"hello"
x
y
z

lst = [100,200,300]
a,b,c = lst
a
b
c

#Similarly sequences with nested tuples can be unpacked
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d

