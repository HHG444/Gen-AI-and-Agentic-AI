from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# Import as Dataframe from web
#df = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/a10.csv', parse_dates=['date'])
#df.head()

# Import as Dataframe from disk (replace git link with path of file on disk)
print("--TS Data--")
dfT = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/a10.csv', parse_dates=['date'])
dfT.head()
print(dfT.head())

#Import it as a pandas Series with the date as index.
#specify the index_col argument in the pd.read_csv()
#ser = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/a10.csv', parse_dates=['date'], index_col='date')
#ser.head()
#print(ser.head())
#Note**the ‘value’ column is placed higher than date to imply that it is a series.

print("--Panel Data--")
dfP = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/MarketArrivals.csv')
dfP = dfP.loc[dfP.market=='MUMBAI', :]
dfP.head()
print(dfP.head())

#Matplotlib to visualise the series
# Draw Plot 1 for dfT
def plot_dfT(dfT, x, y, title="", xlabel='Date', ylabel='Value'):
   #plt.figure(figsize=(16,5), dpi=dpi)
   plt.plot(x, y, color='tab:red')
   plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
   plt.show()

plot_dfT(dfT, x=dfT.index, y=dfT.value, title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.')   







