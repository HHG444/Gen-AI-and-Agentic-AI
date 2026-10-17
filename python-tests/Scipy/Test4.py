# #Working with optimize package
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.OptimizeResult.html
# https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
# Result :
#     x	(ndarray) The solution of the optimization.
#     success	(bool) Whether or not the optimizer exited successfully.
#     status	(int) Termination status of the optimizer. Its value depends on the underlying solver. Refer to message for details.
#     message	(str) Description of the cause of the termination.
#     fun, jac, hess, hess_inv	(ndarray) Values of objective function, Jacobian, Hessian or its inverse 
#     (if available). The Hessians may be approximations, see the documentation of the function in question.
#     nfev, njev, nhev	(int) Number of evaluations of the objective functions and of its Jacobian and Hessian.
#     nit	(int) Number of iterations performed by the optimizer.
#     maxcv	(float) The maximum constraint violation.

import numpy as np
from scipy import optimize

#define function
def f(x):
    return x**2 + 5*np.sin(x)

#minimization of scalar function of one or more variables using bfgs algorithm
#options being set to true will display covergence messages such as
#Current Function Value, Iterations, Function evaluations, Gradient evaluation
optimize.minimize()
minimaValue = optimize.minimize(f,x0=2,method='bfgs',options={'disp':True})


minimaValueWithoutOpt = optimize.minimize(f,x0=2,method='bfgs')
#no convergence messages displayed
minimaValueWithoutOpt

#optimize root of vector function
from scipy.optimize  import root
def rootFunc(x):
    return x + 3.5 * np.cos(x)

rootValue = root(rootFunc, 0.3)
rootValue

#Applying optimize to sin(x) sin(y)
def func(xy): #single argument which is array of all values
    x,y=xy    #unpacking tuple 
    return np.sin(x)*np.sin(y)

optimize.minimize(func, (0.1,-0.1))
#result will show the best value for x as array,nit:no of iterations

#we can also assign 
result = optimize.minimize(func, (0.1,-0.1))
result
result.nit
result.x

