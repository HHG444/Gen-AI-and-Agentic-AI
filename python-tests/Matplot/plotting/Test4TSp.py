
import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

randvals = np.random.randn(1000)
pd.Series(randvals).plot(title='Random White Noise', color='k')
plt.show()