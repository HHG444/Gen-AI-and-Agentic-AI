import pandas as pd

#(Prefered)shortcut to do in one line & parse dates
opsd_dailyN = pd.read_csv('https://raw.githubusercontent.com/ajaykuma/Datasets/master/opsd_germany_daily.txt', index_col=0, parse_dates=True)

# Add columns with year, month, and weekday name
#--(using DatetimeIndex to convert into datetime type)
#--opsd_daily['year'] = pd.DatetimeIndex(opsd_daily['Date']).year

opsd_dailyN['Year'] = opsd_dailyN.index.year
opsd_dailyN['Month'] = opsd_dailyN.index.month
opsd_dailyN['Weekday Name'] = opsd_dailyN.index.weekday_name
print('*' * 50)

# Display a random sampling of 5 rows
print(opsd_dailyN.sample(5, random_state=0))
print(opsd_dailyN.head(3))
print('*' * 50)

#Time-based indexing — using dates and times to intuitively organize and access our data.

print(opsd_dailyN.loc['2017-08-10'])
#Selecting a slice, slice is inclusive of both end points
print(opsd_dailyN.loc['2014-01-20':'2014-01-22'])

#partial-string indexing, where we can 
# select all date/times which partially match a given string.
print(opsd_dailyN.loc['2012-02'])

import matplotlib.pyplot as plt
#using use seaborn styling for our plots
import seaborn as sns
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 4)})

#create a line plot of the full time series of Germany’s daily electricity consumption, using the DataFrame’s plot() method.
opsd_dailyN['Consumption'].plot(linewidth=0.5)


#plot the data as dots instead, and also look at the Solar and Wind time series
cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_dailyN[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')

#plot the time series in a single year
ax = opsd_dailyN.loc['2017', 'Consumption'].plot()
ax.set_ylabel('Daily Consumption (GWh)')

#zoom in further and look at just January and February
ax = opsd_dailyN.loc['2017-01':'2017-02', 'Consumption'].plot(marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)')

#to have vertical gridlines on a weekly time scale 
import matplotlib.dates as mdates
fig, ax = plt.subplots()
ax.plot(opsd_dailyN.loc['2017-01':'2017-02', 'Consumption'], marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)')
ax.set_title('Jan-Feb 2017 Electricity Consumption')

# Set x-axis major ticks to weekly interval, on Mondays
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))

# Format x-tick labels as 3-letter month name and day number
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

#To explore the seasonality of our data with box plots, using seaborn’s boxplot() function to group 
# the data by different 
#time periods and display the distributions for each group. 
fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
    sns.boxplot(data=opsd_dailyN, x='Month', y=name, ax=ax)
    ax.set_ylabel('GWh')
    ax.set_title(name)
# Remove the automatic x-axis label from all but the bottom subplot
if ax != axes[-1]:
    ax.set_xlabel('')

#group the electricity consumption time series by day of the week, 
# to explore weekly seasonality.
sns.boxplot(data=opsd_dailyN, x='Weekday Name', y='Consumption')

#Frequencies

#When the data points of a time series are uniformly spaced in time (e.g., hourly, 
#daily, monthly, etc.), the time series can be associated with a frequency in pandas. 
#freq with a value of 'D', indicates daily frequency. Available frequencies in pandas include hourly ('H'), 
#calendar daily ('D'), business daily ('B'), weekly ('W'), monthly ('M'), quarterly ('Q'), annual ('A'), 
pd.date_range('1998-03-10', '1998-03-15', freq='D')

#create a date range at hourly frequency, specifying the start date and number of periods, 
# instead of the start date and end date.
pd.date_range('2004-09-20', periods=8, freq='H')


opsd_dailyN.index

#create a new DataFrame which contains only the Consumption data for Feb 3, 6, and 8, 2013.
# To select an arbitrary sequence of date/time values from a pandas time series,
# we need to use a DatetimeIndex, rather than simply a list of date/time strings
times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
# Select the specified dates and just the Consumption column
consum_sample = opsd_dailyN.loc[times_sample, ['Consumption']].copy()
consum_sample

# Convert the data to daily frequency, without filling any missings
consum_freq = consum_sample.asfreq('D')
# Create a column with missings forward filled
consum_freq['Consumption - Forward Fill'] = consum_sample.asfreq('D', method='ffill')
consum_freq

#Resampling
#resample the data to a weekly mean time series
# Specify the data columns we want to include (i.e. exclude Year, Month, Weekday Name)
data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
# Resample to weekly frequency, aggregating with mean
opsd_weekly_mean = opsd_dailyN[data_columns].resample('W').mean()
opsd_weekly_mean.head(3)

#comparung
print(opsd_dailyN.shape[0])
print(opsd_weekly_mean.shape[0])

#plot the daily and weekly Solar time series together over a single six-month period to compare them.
# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily and weekly resampled time series together
fig, ax = plt.subplots()
ax.plot(opsd_dailyN.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Solar Production (GWh)')
ax.legend()

#Resample the data to monthly frequency, aggregating with sum totals instead of the mean. 
#Unlike aggregating with mean(), which sets the output to NaN for any period with all missing data, 
#the default behavior of sum() will return output of 0 as the sum of missing data. We use the min_count
#parameter to change this behavior.
# Compute the monthly sums, setting the value to NaN for any month which has
# fewer than 28 days of data
opsd_monthly = opsd_dailyN[data_columns].resample('M').sum(min_count=28)
opsd_monthly.head(3)

#explore the monthly time series by plotting the electricity consumption as a line plot,
#  and the wind and solar power 
#production together as a stacked area plot.
fig, ax = plt.subplots()
ax.plot(opsd_monthly['Consumption'], color='black', label='Consumption')
opsd_monthly[['Wind', 'Solar']].plot.area(ax=ax, linewidth=0)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_ylabel('Monthly Total (GWh)')

#resampling to annual frequency and computing the ratio of Wind+Solar to Consumption 
# for each year.
# Compute the annual sums, setting the value to NaN for any year which has
# fewer than 360 days of data
opsd_annual = opsd_dailyN[data_columns].resample('A').sum(min_count=360)
# The default index of the resampled DataFrame is the last day of each year,
# ('2006-12-31', '2007-12-31', etc.) so to make life easier, set the index
# to the year component
opsd_annual = opsd_annual.set_index(opsd_annual.index.year)
opsd_annual.index.name = 'Year'
# Compute the ratio of Wind+Solar to Consumption
opsd_annual['Wind+Solar/Consumption'] = opsd_annual['Wind+Solar'] / opsd_annual['Consumption']
opsd_annual.tail(3)


# Compute the ratio of Wind+Solar to Consumption
opsd_annual['Wind+Solar/Consumption'] = opsd_annual['Wind+Solar'] / opsd_annual['Consumption']
opsd_annual.tail(3)


#plot the wind + solar share of annual electricity consumption as a bar chart.
# Plot from 2012 onwards, because there is no solar production data in earlier years
ax = opsd_annual.loc[2012:, 'Wind+Solar/Consumption'].plot.bar(color='C0')
ax.set_ylabel('Fraction')
ax.set_ylim(0, 0.3)
ax.set_title('Wind + Solar Share of Annual Electricity Consumption')
plt.xticks(rotation=0)

#Rolling windows
#Rolling windows
# Compute the centered 7-day rolling mean
opsd_7d = opsd_dailyN[data_columns].rolling(7, center=True).mean()
opsd_7d.head(10)

#To visualize the differences between rolling mean and resampling, let’s update our earlier plot of January-June 2017 solar power production to include 
#the 7-day rolling mean along with the weekly mean resampled time series and the original
#  daily data.
# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily, weekly resampled, and 7-day rolling mean time series together
fig, ax = plt.subplots()
ax.plot(opsd_dailyN.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.plot(opsd_7d.loc[start:end, 'Solar'],
marker='.', linestyle='-', label='7-d Rolling Mean')
ax.set_ylabel('Solar Production (GWh)')
ax.legend()

#Trending
#compute the 365-day rolling mean of our OPSD data.
# The min_periods=360 argument accounts for a few isolated missing days in the
# wind and solar production time series
opsd_365d = opsd_dailyN[data_columns].rolling(window=365, center=True, min_periods=360).mean()

#plot the 7-day and 365-day rolling mean electricity consumption, along with the daily time series.
# Plot daily, 7-day rolling mean, and 365-day rolling mean time series
fig, ax = plt.subplots()
ax.plot(opsd_dailyN['Consumption'], marker='.', markersize=2, color='0.6',
linestyle='None', label='Daily')
ax.plot(opsd_7d['Consumption'], linewidth=2, label='7-d Rolling Mean')
ax.plot(opsd_365d['Consumption'], color='0.2', linewidth=3,
label='Trend (365-d Rolling Mean)')
# Set x-ticks to yearly interval and add legend and labels
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Consumption (GWh)')
ax.set_title('Trends in Electricity Consumption')

#trends in wind and solar production.
# Plot 365-day rolling mean time series of wind and solar power
fig, ax = plt.subplots()
for nm in ['Wind', 'Solar', 'Wind+Solar']:
    ax.plot(opsd_365d[nm], label=nm)
    # Set x-ticks to yearly interval, adjust y-axis limits, add legend and labels
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.set_ylim(0, 400)
    ax.legend()
    ax.set_ylabel('Production (GWh)')
    ax.set_title('Trends in Electricity Production (365-d Rolling Means)')
    




