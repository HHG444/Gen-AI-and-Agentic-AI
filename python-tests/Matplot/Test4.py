#Creating Multiple Plots
#import library
import matplotlib.pyplot as plt
from matplotlib import style
#(if using notebook)
#%matplotlib inline

#website traffic data
# no of users/visitors on the website
#Monday web traffic
web_monday = [123,645,950,1290,1630,1450,1034,1295,465,205,80]

#Tuesday web traffic
web_tuesday = [95,680,889,1145,1670,1323,1119,1265,510,310,110]

#wednesday web traffic
web_wednesday = [105,630,700,1006,1520,1124,1239,1380,580,610,230]

#Time distribution(hourly)
time_hrs = [7,8,9,10,11,12,13,14,15,16,17]

#select the style of plot
plt.style('ggplot')

#plotting the website traffic data (X-axis hrs and Y-axis as number of users)
#monday data red color
plt.plot(time_hrs,web_monday,'r',label='monday',linewidth=1)

#Tuesday data green color
plt.plot(time_hrs,web_tuesday,'g',label='tuesday',linewidth=1.5)

#wednesday data red color
plt.plot(time_hrs,web_wednesday,'b',label='wednesday',linewidth=2)

plt.axis([0,20,500,3000])

#set the title of the plot
plt.title('Web site traffic')

#setting label for x and y-axis
plt.xlabel('Hrs')
plt.ylabel('Number of users')
plt.legend()
plt.show()




