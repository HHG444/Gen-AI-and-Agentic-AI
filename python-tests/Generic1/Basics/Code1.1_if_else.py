#1 taking input and evaluating
x = int(input('enter a number:'))

#if elif else
if x>100:
    print('x was greater than expected')
elif x<=100 and x>=50:
    print('x is lesser than 100 but greater than 50')
elif x<50 and x>=20:
    print('x is as expected')
else:
    print('x is below expected')

#2 #checking boolean
name = "john"
age = 20
is_new = False

if(is_new):
    print(name + ' ' + str(age))
else:
    print("he is not new")

#3 
is_published = False
if (is_published == True):
    print(is_published)
else:
    print('its value is not set to True')

print('-'*20)

#comparision operators
temperature = 30
if temperature>30:
    print("its hot")
elif temperature<30:
    print("its not so hot")
#note assignment operator
    if temperature == 20:
        print("its gud")
else:
    print('its ' + str(temperature))

