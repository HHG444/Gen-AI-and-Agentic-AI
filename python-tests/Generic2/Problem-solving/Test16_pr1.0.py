newS = set()
while True:
    line = input()
    while line != 'done':
        newS.add(line)
    if line == 'done':
        break
    elif len(newS) < 5:
        continue
    else:
        print('for now thats enough')
        break
print(sorted(newS))
print('no number given,bye!!')

    
