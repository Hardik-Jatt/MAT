import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(1000)).cumsum()

pd.plotting.lag_plot(data)
plt.title('Lag Plot')
plt.show()
