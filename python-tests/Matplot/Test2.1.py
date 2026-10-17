import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline
#%config InlineBackend,figure_format = 'svg'
pi = np.pi
x = np.linspace(-4*pi, 4*pi, 1000)

#to increase the size
plt.rcParams['figure.figsize'] = (14,6)

#to add labels to your plot
plt.xticks([-4*pi,-2*pi,0,2*pi,4*pi],
['$-4\pi$','$-2\pi$','$0$','$2\pi$','$4\pi$'])

#to increase size of labels(x -axis)
plt.rcParams.update({'font.size':10})

#for y-axis
plt.yticks([0,1],['$0$','$1$'])
plt.ylim(-0.5,1.5)

plt.plot(x, np.sin(x)/x,label="singrph")
#to display legend
plt.legend(loc = 'best',fontsize = 10)

#Adding a title
plt.title('The $sinc$ function')

#adding a origin line
plt.axhline(0, color='black',lw=1)
plt.show()

