import numpy as np
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import nquad

#define functions that we would want to integrate

def f(x):
    return x

#using quad to calculate area under this function i.e. where f(x)=x
area = quad(f,0,2)
print(area)
#result would show (2.0, 2.220446049250313e-14) 
# where 2.0 is the value of integral after quad function was applied
# 2.22... is the estimate of absolute error of the integral (the smaller the better)

#using dblquad to calculate area under x*y
def f(x,y):
    return x*y

area = dblquad(f,0,2,0,5)
print(area)
#result would show (25.0, 2.7755575615628914e-13)

#using lambda to define a function
f = lambda x,y: x*y
area = dblquad(f,0,2,0,5)
print(area)
#result would show (25.0, 2.7755575615628914e-13)

#sometimes our integration may not be constant, say we want to apply lower and upper limit 
# for y , lambda would be more useful to apply limits for constants
y_low_limit = lambda y: y
y_upp_limit = lambda y: y*5

area = dblquad(f,0,2,y_low_limit,y_upp_limit)
print(area)

#result would show (48.000000000000014, 1.0588861835093356e-12)

#using nquad for multiple integration
def f(x,y,z):
    return x*y*z

area = nquad(f,[[0,2],[0,5],[0,5]])
print(area)
#result would show (312.49999999999994, 3.4694469519536134e-12)

#using lambda for nquad
f = lambda x,y,z: x*y*z
area = nquad(f,[[0,2],[0,5],[0,5]])
print(area)
#result would show (312.49999999999994, 3.4694469519536134e-12)






