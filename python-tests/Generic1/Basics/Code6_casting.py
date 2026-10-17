#1 
words = ['hi','hello','cool']
x = str(input("enter a word:"))

#by default input is considered as str
x = (input("enter a word:"))
for i in words:    
    if(i == x):
        print("you entered exact word which is " + x)
#using index to get position of an element
        print('@position ' + str(words.index(i)))
        break
    else:
        print("word entered by you was not word in list")
print("you entered :" + x)

#2
s = ['1', '2', '3', '4']
for i in s:
    print(i,type(i))

for i in s:
    print(int(i),'after casting: ', type(int(i)))

for i in s:
    print(float(i),'after casting: ', type(float(i)))
