#Represent definte integral with plot
#Solve definite integral problems symbolically

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

#to solve integration of x**2 for a limit 0 to 2
x = np.linspace(-1,3,1000)

def f(x) : return x**2

plt.plot(x,f(x))
print(plt.show())

#to see area between curve and x-axis
plt.plot(x,f(x))
plt.axhline(color = 'black') #to add x-axis
print(plt.show())

#using fill between
plt.plot(x,f(x))
plt.axhline(color = 'black')
plt.fill_between(x,f(x),where = [(x>0) and (x<2) for x in x])
#plt.fill_between(x,f(x),where = [(x>0) and (x<2) for x in x],color='green')
print(plt.show())

#to evaluate function and to work symbolically we can use sympy 
#change x to symbol
x
x = sy.Symbol('x')
def f(x) : return x**2
sy.integrate(f(x), (x,0,2))

#define new function and rememeber to convert x back to number
def g(x) : return x**(1/2)

x = np.linspace(-1,1.5,100)

plt.plot(x,f(x))
plt.plot(x,g(x))
print(plt.show())

#to get area between these
plt.plot(x,f(x))
plt.plot(x,g(x))
plt.fill_between(x,f(x),g(x), where = [(x>0) and (x<1) for x in x],color = 'green')
print(plt.show())

#again symbolically doing it
x = sy.Symbol('x')
def f(x) : return x**2
sy.integrate(g(x)- f(x), (x,0,1))





