import pandas as pd
import numpy as np

#option 1
df = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/auction.csv')
df

#option 2 - without header values
df1 = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',header=None)
df1

#option 3
df2 = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',
names=['a', 'b', 'c', 'd', 'e','f','g','h','message'])
df2

#option 4 (making a column as index column)
names=['a', 'b', 'c', 'd', 'e','f','g','h','message']
df3 = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',
      names=names,index_col='message')
df3

#option 5
pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',skiprows=[0, 2, 3])
pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',na_values=['NULL'])

#different sentinels for each column 
#sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
#pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',na_values=sentinels)

#using chunksize /nrows
mydf = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',nrows=5)
mydf = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',chunksize=1000)
type(mydf)
df.head()
df.describe

df1 = pd.read_table('I:\\Trainings\\MyContent\\Books\\resources\\auction.csv',sep=',')
df1.values

#writing data out
df1.to_csv('I:\\Trainings\\MyContent\\Books\\resources\\test.csv')

import sys
df1.to_csv(sys.stdout,sep = '|')
df1.to_csv(sys.stdout,sep = '|',na_rep='NULL')
df1.to_csv(sys.stdout,sep = '|',index=False, header=False)
#df1.to_csv(sys.stdout,sep = '|',index=False, cols =['a','b','c'])




