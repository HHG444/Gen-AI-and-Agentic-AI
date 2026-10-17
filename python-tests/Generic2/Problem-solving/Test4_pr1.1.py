import collections
from pprint import pprint
Scientist = collections.namedtuple('Scientist',['name','field','born','nobel'])
scientists = (Scientist(name='Ada Lovelace',field='math',born=1815,nobel=False),
            Scientist(name='Emmy',field='math',born=1882,nobel=False)
            )

s = filter(lambda x: x.nobel==False,scientists)
next(s)
tuple(filter(lambda x: x.nobel==False,scientists))
fs = tuple(filter(lambda x: x.nobel==False,scientists))
pprint(fs)

for i in scientists:
    if i.nobel==True:
        print(i)
    else:
        print('nthing found')

def sc_filter(x):
    return x.nobel==False

fs1=tuple(filter(sc_filter,scientists))

fs2 = [tuple([x for x in scientists if x.nobel is False])]
pprint(fs2)
fs3 = [tuple(x for x in scientists if x.nobel is False)]
pprint(fs2)




