#to test for seasonality of a time series
#plot the series and check for repeatable patterns in fixed time intervals
#such as auto correlation function ACF plot
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


from pandas.plotting import autocorrelation_plot
df = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/a10.csv')

# Draw Plot
plt.rcParams.update({'figure.figsize':(9,5), 'figure.dpi':120})
autocorrelation_plot(df.value.tolist())
plt.show()
