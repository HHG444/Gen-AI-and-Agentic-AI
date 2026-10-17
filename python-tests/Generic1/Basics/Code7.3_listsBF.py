#Built in functions
#sorted:returns a new sorted list from the elements of any sequence
sorted([7, 1, 2, 6, 0, 3, 2])

test = [7,1,2,6,0,3,2]
type(test)
sorted(test)
test

test.sort()
test

test[0]
test[1]
test[2]

test[0] = 100
test[1] = 200
test

sorted('stock trading')

#getting a sorted list of the unique elements in a sequence
sorted(set('this is just cool empty space'))

mylist = [10,12,13,13,14,15,153,153,1,0]
myset = set(mylist)
myset

mynewset = set()
mydupele = []
type(mynewset)

for i in mylist:
    if i not in mynewset:
        mynewset.add(i)
    else:
        mydupele.append(i)
mynewset
mydupele

#zip:“pairs” up the elements of a number of lists, tuples, or other sequences, to create
#a list of tuples:
seq1 = ['teacher', 'girls', 'boys']
seq2 = ['one', 'two', 'three']
#seq3 = ['one', 'two', 'three']
#x = zip(seq1,seq2,seq3)
x = zip(seq1,seq2)
for i in x:
    print(i)

#zip can take an arbitrary number of sequences (shortest seq chosen)
seq3 = [False, True]
x = zip(seq1, seq2, seq3)
for i in x:
    print(i)

#simultaneously iterating over multiple sequences
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('%d: %s, %s' % (i, a, b))

students = [('Nolan', 'Ryan'), ('Roger', 'Clemens')]
first_names, last_names = zip(*students)

first_names
last_names

#reversed:iterates over the elements of a sequence in reverse order
list(reversed(range(10)))

#enumerate: when iterating over a sequence to want to keep 
# track of the index of the current item

#for i, value in enumerate(collection):
    # do something with value

some_list = ['foo', 'bar', 'baz']
mapping = dict((v, i) for i, v in enumerate(some_list))
mapping
type(mapping)

result = [n in some_list for n in some_list]
result

#using collections
import collections
l = ["he","she","he","she","he"]
print(sorted(collections.Counter(l)))
