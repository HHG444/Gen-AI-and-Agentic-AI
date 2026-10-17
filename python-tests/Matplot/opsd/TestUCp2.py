import pandas as pd
opsd_daily = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/opsd_germany_daily.txt')
print(opsd_daily.shape)
print(opsd_daily.head(3))

print(opsd_daily.dtypes)
print('*' * 50)
#if Date column is in the correct data type, let’s set it as the DataFrame’s index.
opsd_daily = opsd_daily.set_index('Date') #<--This will not work as Date is already '
#an index of object type

print(opsd_daily.head(3))
print(opsd_daily.dtypes) #shows index as Object Type
#Date            object
#Consumption    float64
#Wind           float64
#Solar          float64
#Wind+Solar     float64
#dtype: object

print(opsd_daily.index) #RangeIndex(start=0, stop=4383, step=1)
print(opsd_daily.columns)
print('*' * 50)

opsd_daily["Date"]= pd.to_datetime(opsd_daily["Date"])
opsd_daily.dtypes
#so we can use 'DatetimeIndex' to add columns in DF
opsd_daily['year'] = pd.DatetimeIndex(opsd_daily['Date']).year
opsd_daily['month'] = pd.DatetimeIndex(opsd_daily['Date']).month

#..continue working with your TS Dataset via this DF

#Alternatively
opdf = pd.DataFrame(opsd_daily)
opdf.head()           
opdf['year'] = pd.DatetimeIndex(opdf['Date']).year
#This will not work as here Index is in Object type
opdf.index
#RangeIndex(start=0, stop=4383, step=1)
opdf.dtypes
#Date            object
#Consumption    float64
#Wind           float64
#Solar          float64
#Wind+Solar     float64
#dtype: object

#convert to datetime format
opdf["Date"]= pd.to_datetime(opdf["Date"])
opdf.dtypes
#Date           datetime64[ns]

#now looking into opsd_daily shows
opsd_daily.dtypes
#Date           datetime64[ns]

#so we can use 'DatetimeIndex' to add columns in DF
opsd_daily['year'] = pd.DatetimeIndex(opsd_daily['Date']).year
opsd_daily['month'] = pd.DatetimeIndex(opsd_daily['Date']).month
opsd_daily.head()

#now we can start working..

