from dateutil.parser import parse 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Import data
ap = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/AirPassengers.csv')
ap.head(n=5)
x = ap['date'].values
y1 = ap['value'].values

# n = pd.DatetimeIndex(ap['date']).year.values
# n
# xmax=max(pd.DatetimeIndex(ap['date']).year)
# xmax
# Plot

def plot_ap(ap, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.fill_between(x, y1=y1,y2=-y1, alpha=0.5, linewidth=2, color='green')
    plt.ylim(-800, 800)
    plt.title('Air Passengers (Two Side View)', fontsize=16)
    plt.show()
plot_ap(ap, x=ap.index, y=ap.value) 

#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

#Since its a monthly time series and follows a certain repetitive pattern every year,
# you can plot each year as a separate line in the same plot. This lets you compare 
# the year wise patterns side-by-side.
