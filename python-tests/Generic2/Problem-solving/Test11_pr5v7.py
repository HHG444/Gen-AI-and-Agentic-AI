# file: test.py
import collections
import timeit

def thg435(l):
    return [x for x, y in collections.Counter(l).items() if y > 1]

def moooeeeep(l):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in l if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    return list( seen_twice )

def RiteshKumar(l):
    return list(set([x for x in l if l.count(x) > 1]))

def JohnLaRooy(L):
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for item in L:
        if item in seen:
            seen2_add(item)
        else:
            seen_add(item)
    return list(seen2)

l = [1,2,3,2,1,5,6,5,5,5]*100

#
# python -mtimeit -s 'import test' 'test.JohnLaRooy(test.l)'
#10000 loops, best of 3: 74.6 usec per loop
#$ python -mtimeit -s 'import test' 'test.moooeeeep(test.l)'
#10000 loops, best of 3: 91.3 usec per loop
#$ python -mtimeit -s 'import test' 'test.thg435(test.l)'
#1000 loops, best of 3: 266 usec per loop
#$ python -mtimeit -s 'import test' 'test.RiteshKumar(test.l)'
#100 loops, best of 3: 8.35 msec per loop
#Interestingly, besides the timings itself, also the ranking slightly changes 
# when pypy is used. Most interestingly, the Counter-based approach benefits hugely 
# from pypy's optimizations, whereas the method caching approach I have suggested 
# seems to have almost no effect.
#$ pypy -mtimeit -s 'import test' 'test.JohnLaRooy(test.l)'
#100000 loops, best of 3: 17.8 usec per loop
#$ pypy -mtimeit -s 'import test' 'test.thg435(test.l)'
#10000 loops, best of 3: 23 usec per loop
#$ pypy -mtimeit -s 'import test' 'test.moooeeeep(test.l)'
#10000 loops, best of 3: 39.3 usec per loop

#Apparantly this effect is related to the "duplicatedness" of the input data. I have set l = [random.randrange(1000000) for i in xrange(10000)] and got these results:
#$ pypy -mtimeit -s 'import test' 'test.moooeeeep(test.l)'
#1000 loops, best of 3: 495 usec per loop
#$ pypy -mtimeit -s 'import test' 'test.JohnLaRooy(test.l)'
#1000 loops, best of 3: 499 usec per loop
#$ pypy -mtimeit -s 'import test' 'test.thg435(test.l)'
#1000 loops, best of 3: 1.68 msec per loop