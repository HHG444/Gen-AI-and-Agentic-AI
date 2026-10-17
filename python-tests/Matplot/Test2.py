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
#plt.plot(time_hrs,web_customers)
plt.plot(time_hrs,web_customers,color= 'g',linestyle = '--',linewidth=2.5
,label='line one')

#setting the desired axis to interpret the required result
#Axis is to define the range on x axis and y axis using axis method()
#X-axis is set to range from 6.5 to 17.5, Y-axis is set to range from 50 to 2000
#plt.axis(6.5,17.5,50,2000)

#set the title of the plot
plt.title('Web site traffic')

#setting label for x and y-axis
plt.xlabel('Hrs')
plt.ylabel('Number of users')
plt.legend()
plt.show()
#==================



