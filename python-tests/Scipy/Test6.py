#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
#Non-Linear curve fitting  using python
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
#should also have first paramter as xdata points
def func(x,a,b):
    return a*np.exp(b*x)
    #return a*x+b --for linear functions however might not return effecient sol

#experimental x and y data points
xData = np.array([1,2,3,4,5])
yData = np.array([1,9,50,300,1500])

#Plot experimental data points
plt.plot(xData,yData, 'bo', label = 'experimental-data')
plt.show()

#Initial guess for paramters can be provided if needed
#initialGuess = [1.0,1.0]

#perform the curve-fit
#popt gets the optimized paramters for fitted function
#pcov gets covariance matrix,2D array 
popt,pcov = curve_fit(func,xData,yData)
#popt,pcov = curve_fit(func,xData,yData,initialGuess)

print(popt)

#x values for fitted function
xFit = np.arange(0.0,0.5,0.01)

#plot the fitted function
#plt.plot(xFit, func(xFit, *popt), 'r', label = 'fit params: a = %5.3f, b=%5.3f' & tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()