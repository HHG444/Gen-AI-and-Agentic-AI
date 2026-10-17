from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# Draw Plot for ser
ser = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets_For_Work/refs/heads/main/a10.csv', parse_dates=['date'], index_col='date')
ser
ser.reset_index(inplace=True)


# Prepare data
ser['year'] = [d.year for d in ser.date]
ser

ser['month'] = [d.strftime('%b') for d in ser.date]
ser
years = ser['year'].unique()
ser.head(n=5)

# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# Draw Plot

for i, y in enumerate(years):
    if i > 0:        
        plt.plot('month', 'value', data=ser.loc[ser.year==y, :], color=mycolors[i], label=y)
        plt.text(ser.loc[ser.year==y, :].shape[0]-.9, ser.loc[ser.year==y, 'value'][-1:].values[0], y, fontsize=12, color=mycolors[i])

# Decoration
plt.gca().set(xlim=(-0.3, 11), ylim=(2, 30), ylabel='$Drug Sales$', xlabel='$Month$')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Seasonal Plot of Drug Sales Time Series", fontsize=20)
plt.show()


#There is a steep fall in drug sales every February, rising again in March, 
# falling again in April and so on. Clearly, the pattern repeats within a given year, 
# every year.

#However, as years progress, the drug sales increase overall. You can nicely visualize
#  this trend and how it varies each year in a nice year-wise boxplot. Likewise, 
# you can do a month-wise boxplot to visualize the monthly distributions.

