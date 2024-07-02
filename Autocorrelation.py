import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(1000)).cumsum()

pd.plotting.autocorrelation_plot(data)
plt.title('Autocorrelation Plot')
plt.show()
