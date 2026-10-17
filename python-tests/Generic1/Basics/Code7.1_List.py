#Lists are variable-length and their contents can be modified
#[] or list()
#1 
emptylst = []
print(emptylst)

#check if list is empty
if not emptylst:
    print('its empty')

#2
a_list = [2, 3, 7, None]
for i in a_list:
    print(type(i))
type(a_list)

b_list = ('cool', 'bar', 'jazz')
type(b_list)

c_list = list(b_list)
type(c_list)

a_list
b_list
c_list

#3 working with lists
numbers = [5,2,5,1,7,4]
numbers.append(100)
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(5)
print(numbers)

#emptying list
numbers.clear()
print(numbers)

#removing element based on index
numbers = [1,5,2,5,1,7,4]
numbers.pop(4)
print(numbers)

#checking existence of a element
print(50 in numbers)

#find a count
print(numbers.count(5))

#sorting a list
numbers.sort() #shows none which is an object in python
print(numbers)

#sorting in descending order
numbers.reverse()
print(numbers)

#creating a copy 
#any operation on original list doesnt affect the copy
numbers2 = numbers.copy()

#concatenating and combining lists
newl = [4, None, 'foot'] + [7, 8, (2, 3)]
newl

#appending multiple elements to list i.e. entending a list
y = ['hello','cool',100]
newl.extend(y)
newl

#4 list concatenation is a compartively expensive operation since a new list must
#be created and the objects copied over. Using extend to append elements
#to an existing #list, especially if you are building up a large list, 
#is usually preferable.

#Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[::2]

#pass -1 for reversing a list or tuple
seq[::-1]

#creating a list
x = str(input("enter a word:"))
#print(x)
y = str(input("enter another word:"))
#print(y)
mystring = [x,y]

for i in mystring:
    print(i)
    
print(mystring)

#5 Finding greatest number in the list
numbers = [10,3,6,2,8,4]
print(max(numbers))

#assuming number at 0 index is max
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f" max is {max}")

#6 Dimensional lists in Python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

matrix[0][1] = 20

print(matrix[0][1])

#iterating through this list
for row in matrix:
    for item in row:
        print(item)
print('-' * 30)







