#import libraries
import numpy as np
import pandas as pd
#create dataframe from dict of series for summer olympics : 1996 to 2012
olympic_series_participation = pd.Series([205,204,201,200,197],index=[2012,2008,2004,2000,1996])
olympic_series_country = pd.Series(['London','Beijing','Athens','Sydney','Atlanta'],
                                index = [2012,2008,2004,2000,1996])
df_olympic_series= pd.DataFrame({'No of participating countries':olympic_series_participation,
'Host Cities':olympic_series_country})
print(df_olympic_series)
#view dataframe describe
print(df_olympic_series.describe)
#view top 2 records
print(df_olympic_series.head(2))

#view last 3 records
print(df_olympic_series.tail(3))
#view indexes of dataset
print(df_olympic_series.index)

#view columns of dataset
print(df_olympic_series['Host Cities'])

#data selection no of participating countries
print(df_olympic_series['No of participating countries'])

#select label-location based access by label
print(df_olympic_series.loc[2012])

#Integer-location based indexing by position
print(df_olympic_series.iloc[0:2])

#Integer location based data selection by index value
print(df_olympic_series.iat[3,1])

#select data element by condition where number of participated countries are more than 200
#use boolean expression
print(df_olympic_series[df_olympic_series['No of participating countries']>200])

