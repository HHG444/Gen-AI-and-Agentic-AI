import pandas as pd
power = pd.read_csv("I:\\GitContent\\Datasets\\Datasets\\power.csv")


power.columns
df = pd.DataFrame(power)
df.index   #shows RangeIndex(start=0, stop=37623, step=1
df.columns
df.head()
df.agg({'VALUE':['mean']}),
df.agg({'VALUE':['max']}),
df.agg({'VALUE':['min']}),
df.agg({'VALUE':['std']})
df['year'] = pd.DatetimeIndex(df['START_DATE']).year
df.head
df.columns
df['month'] = pd.DatetimeIndex(df['START_DATE']).month
df.head
df.columns
df['day'] = pd.DatetimeIndex(df['START_DATE']).day
df.head
df.columns
df.groupby(['year']).size()
df.groupby(['year']).count()
df.groupby(['year']).agg({'VALUE':['mean']})