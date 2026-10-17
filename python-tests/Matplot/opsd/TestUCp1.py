import pandas as pd
#to_datetime() automatically infers a date/time format based on the input.
x = pd.to_datetime('2018-01-15 3:45pm')
print(x)
y = pd.to_datetime('7/8/1952')
print(y)

#we can use the dayfirst parameter to tell pandas to interpret the date 
z = pd.to_datetime('7/8/1952', dayfirst=True)
print(z)

#we supply a list or array of strings as input to to_datetime(), it returns a 
# sequence of date/time values in a DatetimeIndex object
a = pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'])
print(a)
#Note**DatetimeIndex above, the data type datetime64[ns] indicates that 
# the underlying data is stored as 64-bit integers, in units of nanoseconds (ns).

#If we’re dealing with a sequence of strings all in the same date/time format, we can 
# explicitly specify it with the format parameter. For very large data sets, 
# this can greatly speed up the performance # of to_datetime() compared to the 
# default behavior, where the format is inferred separately for each individual string.
b = pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y')
print(b)

#pandas.to_datetime(arg, errors=’raise’, dayfirst=False, yearfirst=False, utc=None, 
# box=True, format=None, exact=True, unit=None, infer_datetime_format=False, 
# origin=’unix’, cache=False)
print('*'*60)
import pandas as pd
Test = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/opsd_germany_daily_withTStamp.txt')
print(Test.columns)
print(Test.dtypes)
print(Test.head(3))

Test["Date"]= pd.to_datetime(Test["Date"])
print(Test.dtypes)

Test['Time'] = pd.DatetimeIndex(Test['Date']).time
print(Test.head(3))

Test['Hour'] = pd.DatetimeIndex(Test['Date']).hour
print(Test.head(3))

#explore pd.timestamp







