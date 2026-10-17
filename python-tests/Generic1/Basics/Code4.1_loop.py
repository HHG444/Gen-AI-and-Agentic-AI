#1 For loops
teststring = "earth is round"

for i in teststring:
    print(i)

for i in teststring:
    print(i,end=',')

#whether a character is alphabet or not
for i in teststring:
    if i.isalpha():
        print(i,end=',')

#2 for loop example (when working with list)
words = ['hello','cool','test','why']
for w in words:
    if w == 'hello':
        print('word found')
    else:
        print('word not same as presented')
print('-'*10)

#Using break
for w in words:
    if w == 'hello':
        print('word found')
        break
    else:
        print('word not same as presented')
print('-'*10)

#Using continue
for w in words:
    if w == 'hello':
        print('word found')
        continue
    else:
        print('word not same as presented')
print('-'*10)

#3 checking if word starts with vowel
for w in words:
    if w[0] in ('a','e','i','o','u'):
        print('first letter is a vowel')
    else:
        print('vowel not found as frst letter of word')
print('-' * 30)

#4 using other functions
#Map()
"""The map() function is used to apply a given function to every item 
of an iterable, such as a list or tuple, and returns a 
map object (which is an iterator)."""

print(list(map(lambda n: n.upper(),words)))
print(list(map(lambda n: (n[0],n),words)))
print('-' * 30)

#We can define function and apply using map(), shown later.

#5 converting list of strings into list of integers
s = ['1', '2', '3', '4']
for i in s:
    print(i,type(i))

res = map(int, s)

#check type of res & list elements
print(list(res),"\n",type(res))
print('-' * 30)

#5 working with range
x = range(0,10)
for n in x:
    if n<=6:
        print(n)
    else:
        print('stop!')
        break
print('-' * 30)

#
x = range(101,110,2)
for n in x:
    if( n > 103):
        print(n)
    else:
        print("n is not bigger than 100 so ignoring it")
print('-' * 30)

#applying map
print(map(lambda n: n*2,x))
print(list(map(lambda n: n*2,x)))
print('-' * 30)

# Looping & evaluating
stock_prices = [11,12,13,15,19]
total = 0

for price in stock_prices:
    total += price

print(f"Total: {total}")
avgprice = total/len(stock_prices)
print(f"Avgprice: {avgprice}")
print('-' * 30)

#Nested Loops
#Generating coordinates
for x in range(4):
    for y in range(2):
        print(f'({x},{y})')

nums = [1,2,3,4,5]
for i in nums:
    for j in nums:
        print(i*j,end=',')

#Printing a pattern
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)

#Printing a pattern using nested loops
for i in numbers:
    output = ''
    for n in range(i):
        output += 'x'
    print(output)
print('-' * 30)


