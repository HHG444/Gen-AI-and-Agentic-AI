#Functional programming

scientists = [
    {'name':'Ada Lovelace','field':'math','born':1815,'nobel': False},
    {'name':'Emmy Noether','field':'math','born':1882,'nobel': False}
]
type(scientists[0])

scientists[0]['name']="Eda Lovelace"
scientists

#if wrong key, adds new entry
scientists[0]['nime']="Eda Lovelace"
scientists

import collections
Scientist = collections.namedtuple('ScTest',['name','field','born','nobel'])
Scientist

Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False)
ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)
ada.name
ada.field
ada.born
ada.nobel


scientists = [Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
            Scientist(name='Emmy',field='math',born=1882,nobel=False)
            ]
scientists
del scientists[0]
scientists
type(scientists)

scientists1 = (Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
            Scientist(name='Emmy',field='math',born=1882,nobel=False)
            )
type(scientists1)

x = ['a','b','c','d']
x[0] = 'b'
del x[0]
x.append('g')
x.extend('t')
x

type(x)

import collections
Scientist = collections.namedtuple('ScTest',['name','field','born','nobel'])
Scientist

mydata = (Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
Scientist(name='Emy',field='sc',born=1825,nobel=True),
Scientist(name='Marie',field='math',born=1915,nobel=False),
Scientist(name='Ty nyk',field='math',born=1855,nobel=True),
Scientist(name='robin',field='chemistry',born=1885,nobel=False),
Scientist(name='Sally',field='math',born=1805,nobel=False),)

y = tuple(filter(lambda n : n.noble is True),mydata)
type(y)
from pprint import pprint
pprint(y)
#or
for i in y:
    print(i)
#or











