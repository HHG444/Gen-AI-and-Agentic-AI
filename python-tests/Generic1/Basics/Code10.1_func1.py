#Working/defining functions

#1
def testf():
    print("hello")

testf()

def testf():
    return 2*2

testf()

#2
def myfunc(x):
    if(x == "MrRight"):
        print("welcome")
    else:
        print("you are not authorized")

myfunc("MrRights")
myfunc("sean")

print('-'*10)

#greet_user() #'greet_user' is not defined
#3
def greet_user():
    print("hi there!")
    print("welcome aboard!")

print("start")
greet_user()
print("finish")
print('-'*40)

#4
def greet_user2(name):
    print(f'Hi {name}!')
    print('Welcome aboard')

print("start")
greet_user2("John")
greet_user2("Johny")
print("finish")
print('-'*40)

#5
def greet_user2(fname,lname):
    print(f'Hi {fname} {lname}!')
    print('Welcome aboard')
#arguments to be passed are positional arguments
greet_user2("john","smith")

print('-'*40)
#keyword arguments imprve readability and order doesnt matter

#6
greet_user2("john",lname="smith")
print('*'*40)

#keyword arguments always come after positional arguments
greet_user2("smith",lname="johny")


#6 - define function
# calc_cost(total=50,shipping=5,discount=0.10)

#7
#Functions thats return values
def square(number):
    return number * number #if no return is used, prints None (default value)
result = square(2)
print(result)
#or
print(square(3))





