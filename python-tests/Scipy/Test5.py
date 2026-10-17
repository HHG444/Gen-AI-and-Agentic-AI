#Constrained optimization example
#Box volume optimization with Scipy.Minimize

#problem: We have a box and we want to maximize the volume by changing
#width,lenght and height of the box,while surface area of box stays less than 10

#find equations to describe our box i.e. 
#volume = l*w*h and surface area = (2*l*w)+(2*l*h)+(2*w*h)

import numpy as np
from scipy.optimize import minimize


#def function to calcuate volume of box
def calcVolume(x):
    length = x[0]
    width = x[1]
    height = x[2]
    volume = length * width * height
    return volume

def calcSurface(x):
    length = x[0]
    width = x[1]
    height = x[2]
    surfaceArea = 2*length*width + 2*length*height + 2*height*width
    return surfaceArea

#def objective function for optimization
#We wanted to maximize the volume, returning negative volume.BY minimizing the negative 
#volume ,we are actually maximizing the volume of box

def objective(x):
    return -calcVolume(x)

#create a function that returns our constraints
def constraint(x):
    return 100 - calcSurface(x)

#scipy requires constraints to be loaded in a dictionary
cons = ({'type': 'ineq', 'fun':constraint})

#set intial guess values for box dimensions
lengthGuess = 10
widthGuess = 10
HeightGuess = 10

#load guess values into a numpy array
x0 = np.array([lengthGuess,widthGuess,HeightGuess])

#call scipy minimize to solve our optimization problem
#call solver to minimize the objective function given the constraints
#using SLSQP method as it is the only for solving constraint non-linear optimization
sol = minimize(objective,x0,method='SLSQP',constraints=cons,options={'disp':True})

#retrieve optimized box sizing and volume
x0Opt = sol.x
volumeOpt = -sol.fun
volumeOpt

#calculate surface area with optimized values just to double check
surfaceAreaOpt = calcSurface(x0Opt)

#Print results
print('Length: ' + str(x0Opt[0]))
print('Width: ' + str(x0Opt[1]))
print('Height: ' + str(x0Opt[2]))
print('Volume: ' + str(volumeOpt))
print('Surface Area: ' + str(surfaceAreaOpt))

#Summarizing
#Describe system
#Model system using equations
#Define objective function
#Define constraints
#Understand variables and appropriate method that will be used
#Optimize objective function with given constraints