print('new code with finishing iterations with continue')
while True:
    line = input('$ ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done!')
