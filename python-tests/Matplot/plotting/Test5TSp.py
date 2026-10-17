#Detrend a time series
# Using scipy: Subtract the line of best fit
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from scipy import signal
df = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/a10.csv', parse_dates=['date'])
detrended = signal.detrend(df.value.values)
plt.plot(detrended)
plt.title('Drug Sales detrended by subtracting the least squares fit', fontsize=16)
plt.show()
