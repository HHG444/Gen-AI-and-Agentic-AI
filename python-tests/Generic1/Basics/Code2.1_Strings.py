#1 Working with strings
teststring = "earth is round"

#using built in functions
print(len(teststring)) #len is general purpose function


#using . operator to list methods(as in OOP)
#ie functions with specifically belong to smthing

print(
teststring.upper(),
teststring.lower(),
teststring.title(),
teststring.swapcase(),
teststring.startswith('r'))

#2 Evaluating
teststring.endswith('e')
teststring.find('round')
print(teststring.find('e')) #prints index of this element
print(teststring.replace('earth','Earth'))
print('Earth' in teststring)
teststring.replace('earth','our earth', 1)
teststring.count('earth')

#3
print(teststring.upper(),end=' |')
print(teststring.lower(),end=' ,')
print(teststring.title())
print(teststring.swapcase())
print(teststring.startswith('r'))

#4 Slicing
print(teststring[0:5])
print(teststring[9:0])



