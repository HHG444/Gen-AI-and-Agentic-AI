#import numpy for generating random numbers
import numpy as np

#import matplotlib library
import matplotlib.pyplot as plt

#use style class to set the grid style
from matplotlib import style

#(if using notebook)
#%matplotlib inline

#generate random numbers
randomNumber = np.random.rand(10)

#view the random numbers
print(randomNumber)

#select the style of plot
style.use('ggplot')

#plot the random number (set labels of coordinates, title of plot, legend and line width)
plt.plot(randomNumber, 'r',label='line one',linewidth=2)

#x axis is number of random numbers (index)
plt.xlabel('Range')
#y axis is actual random number
plt.ylabel('Numbers')
#Title of plot
plt.title('First Plot')

plt.legend()
plt.show()






