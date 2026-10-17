#Scipy sub-package statistics
# Here, we’ll use functions for normal distribution. 
# It’s a statistical way to find the real values of random variables whose distributions 
# are unknown. 
# Both CDF and PDF accept loc and scale as arguments to adjust the location and scale 
# of the data distribution. 
# For example, standard normal distribution 
# location is the mean and scale is the standard deviation. 
# CDF:Cumulative Distribution Function- This helps describe the probability 
# that for any 10 continuous random variables, the values of the variables are less than 
# or equal to the argument of the function. 
# PDF:Probability Density Function for random variables:


#import norm for normal distribution
from scipy.stats import norm

#rvs for random variables

norm.rvs(loc=0,scale=1,size=10)

#cumulative distribution function
norm.cdf(5,loc=1,scale=2)

#probability density function
norm.pdf(9,loc=0,scale=1)