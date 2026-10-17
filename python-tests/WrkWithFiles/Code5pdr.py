import pandas as pd
import numpy as np
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('<path>tseries.csv')

Series.from_csv('<path>tseries.csv', parse_dates=True)

