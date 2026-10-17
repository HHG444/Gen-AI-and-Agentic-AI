#print
def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = (x for x in seq if x in seen or seen_add(x))
    return list( seen_twice)
a = [1,2,2,3,3,4,5,6]
print(list_duplicates(a))

