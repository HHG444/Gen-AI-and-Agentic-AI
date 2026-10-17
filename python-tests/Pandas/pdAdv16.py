# importing pandas as pd 
import pandas as pd 
  
# Create the Timestamp object 
ts = pd.Timestamp(2017, 1, 15, 12) 
ts1 = pd.Timestamp(year = 2009, month = 10,  
          day = 21, tz = 'Europe/Berlin') 
  
# Print the Timestamp object 
print(ts)
print(ts1)

# return day of the week 
print(ts.dayofweek)
print(ts1.dayofweek) 