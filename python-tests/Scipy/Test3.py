from scipy import integrate
from scipy import cluster
from scipy import optimize
from scipy import linalg

#help(cluster)
help(optimize)
#help(linalg)

#to perform quad integration on function x from limit 0 to 1
#import quad library from integrate sub package
from scipy.integrate import quad

#define function which will return the function value , for integration of x
def integrateFunction(x):
    return x
   
#perform quad inetgration for function of x for limit 0 1o 1
quad(integrateFunction,0,1)

#define a function for ax+b which will need to declare values for a and b
def integrateFn(x,a,b):
    return x*a+b
a= 3
b= 2

#pass function and limits for the integration
quad(integrateFn,0,1,args=(a,b))

import scipy.integrate as integrate
def f(x,y):
    return x+y
#use dblquad for double integration 
#using lambda to help with multiple integration

#using built in lambda functions to perform multiple integration,
#here lambda is used to define the range of integration
#here since lambda x is 2, it will perform integration on the first integration
integrate.dblquad(f,0,1,lambda x: 0, lambda x:2)

