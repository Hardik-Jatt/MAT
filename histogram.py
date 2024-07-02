import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

# Plot
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
