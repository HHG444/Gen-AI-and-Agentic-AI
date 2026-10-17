#Creating 2d plot
#import library
import matplotlib.pyplot as plt
from matplotlib import style
#(if using notebook)
#%matplotlib inline

#website traffic data
# no of users/visitors on the website
web_customers = [123,645,950,1290,1630,1450,1034,1295,465,205,80]

#time distribution (hourly)
time_hrs = [7,8,9,10,11,12,13,14,15,16,17]

#select the style of plot
style.use('ggplot')

#plotting the website traffic data (X-axis hrs and Y-axis as number of users)
#using alpha value for transparency control
plt.plot(time_hrs,web_customers,alpha=.4)


#set the title of the plot
plt.title('Web site traffic')

#Annotate
plt.annotate('Max',ha='center',va='bottom',xytext=(8,1500),xy=(11,1630),arrowprops={'facecolor':'green'})
#setting label for x and y-axis
plt.xlabel('Hrs')
plt.ylabel('Number of users')
plt.legend()
plt.show()